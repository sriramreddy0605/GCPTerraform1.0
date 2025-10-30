# rapido_split_ride_wallet.py
# Feature: Split Ride for Long Distance + Wallet Auto-Deduction
# Author: Sudula Sriram Reddy
# Description: This feature calculates fare distribution for long-distance shared rides,
# and deducts the amount automatically from each rider’s wallet balance.

class Rider:
    def __init__(self, name, distance, wallet_balance):
        self.name = name
        self.distance = distance
        self.wallet_balance = wallet_balance
        self.share = 0

    def deduct_fare(self, amount):
        if amount > self.wallet_balance:
            print(f"⚠️ {self.name} has insufficient balance! Needs ₹{amount - self.wallet_balance} more.")
        else:
            self.wallet_balance -= amount
            print(f"💸 {self.name} paid ₹{amount}. Remaining wallet: ₹{self.wallet_balance}")


class RapidoRide:
    def __init__(self, total_fare):
        self.total_fare = total_fare
        self.riders = []

    def add_rider(self, rider):
        """Add a Rider object"""
        self.riders.append(rider)

    def split_fare(self):
        """Split total fare based on distance"""
        total_distance = sum(r.distance for r in self.riders)
        for r in self.riders:
            r.share = round((r.distance / total_distance) * self.total_fare, 2)
        return self.riders

    def deduct_from_wallets(self):
        """Automatically deduct each rider’s fare share"""
        for r in self.riders:
            r.deduct_fare(r.share)


# Example usage
if __name__ == "__main__":
    ride = RapidoRide(total_fare=500)  # Long-distance ride total fare

    # Add riders (name, distance travelled in km, wallet balance)
    ride.add_rider(Rider("Rider A", 30, 300))
    ride.add_rider(Rider("Rider B", 50, 600))
    ride.add_rider(Rider("Rider C", 20, 150))

    split_details = ride.split_fare()

    print("\n🚴‍♂️ Rapido Long Distance Split Ride Summary:")
    for r in split_details:
        print(f"{r.name} pays ₹{r.share} for {r.distance} km")

    print("\n💰 Deducting from wallets:")
    ride.deduct_from_wallets()
