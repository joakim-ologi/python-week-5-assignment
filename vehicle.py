class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

# Testing polymorphism
vehicles = [Car(), Plane()]

for vehicle in vehicles:
    vehicle.move()
