class Smartphone:
    def __init__(self, brand, model, battery_capacity):
        self.brand = brand
        self.model = model
        self.battery_capacity = battery_capacity  # in mAh
        self.battery_level = 100  # battery level percentage

    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def charge(self, amount):
        self.battery_level = min(100, self.battery_level + amount)
        print(f"Charging... Battery level is now {self.battery_level}%")

    def use_app(self, app_name, minutes):
        battery_drain = minutes * 2  # drains 2% per minute of app use
        if self.battery_level - battery_drain < 0:
            print("Battery too low to use the app.")
        else:
            self.battery_level -= battery_drain
            print(f"Using {app_name} for {minutes} minutes. Battery level now {self.battery_level}%.")


# Inheritance - Subclass for Gaming Smartphone with extra features
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, battery_capacity, cooling_system):
        super().__init__(brand, model, battery_capacity)
        self.cooling_system = cooling_system  # e.g., "Liquid cooling"

    def activate_cooling(self):
        print(f"{self.brand} {self.model} cooling system activated: {self.cooling_system}")

    # Overriding use_app to add special gaming mode
    def use_app(self, app_name, minutes):
        if app_name.lower() == "game":
            battery_drain = minutes * 5  # gaming drains more battery
            if self.battery_level - battery_drain < 0:
                print("Battery too low to play games.")
            else:
                self.battery_level -= battery_drain
                print(f"Playing games for {minutes} minutes. Battery level now {self.battery_level}%. Gaming mode ON.")
        else:
            super().use_app(app_name, minutes)

