class RapidoRide:
    def __init__(self, total_fare):
        self.total_fare = total_fare
        self.riders = []

    def add_rider(self, name, distance):
        """Add rider details"""
        self.riders.append({"name": name, "distance": distance})

    def split_fare(self):
        """Split fare proportionally based on distance traveled by each rider"""
        total_distance = sum(r["distance"] for r in self.riders)
        for rider in self.riders:
            rider["share"] = round((rider["distance"] / total_distance) * self.total_fare, 2)
        return self.riders


# Example usage
if __name__ == "__main__":
    ride = RapidoRide(total_fare=200)
    ride.add_rider("Rider A", 6)
    ride.add_rider("Rider B", 4)
    ride.add_rider("Rider C", 10)

    split_details = ride.split_fare()

    print("🚴‍♂️ Rapido Bike Taxi Split Ride Summary:")
    for r in split_details:
        print(f"{r['name']} pays ₹{r['share']} for {r['distance']} km")
