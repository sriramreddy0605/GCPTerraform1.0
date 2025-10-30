terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.0.0"
    }
  }
}

provider "google" {
  project = "baseinfra-476708"    # <-- replace with your actual GCP project ID
  region  = "us-central1"
  zone    = "us-central1-a"
}

#  Define the VPC network first
resource "google_compute_network" "vpc_network" {
  name                    = "terraform-vpc"
  auto_create_subnetworks = true
}

#loud Storage Bucket
resource "google_storage_bucket" "my_bucket" {
  name          = "my-gcp-terraform-bucket-sriram-476708"
  location      = "US"
  storage_class = "STANDARD"
}

# Persistent Disk
resource "google_compute_disk" "extra_disk" {
  name  = "terraform-disk"
  type  = "pd-standard"
  zone  = "us-central1-a"
  size  = 10
}

# Attach disk to VM
resource "google_compute_attached_disk" "attach_disk" {
  instance = google_compute_instance.vm_instance.id
  disk     = google_compute_disk.extra_disk.id
}

resource "google_compute_instance" "vm_instance" {
  name         = "terraform-instance"
  machine_type = "e2-micro"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = google_compute_network.vpc_network.name
    access_config {} # for external IP
  }

  metadata_startup_script = "echo Hello from Terraform > /var/tmp/startup.txt"
}

