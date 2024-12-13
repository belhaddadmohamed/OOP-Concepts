# Inheritance
# Definition: Allows one class (child) to inherit the properties and methods of another class (parent).
# Purpose: Promotes code reuse and establishes relationships between classes.


class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def drive(self):
        print(f"{self.brand} is driving at {self.speed} km/h")


class Car(Vehicle):
    def __init__(self, brand, speed, doors):
        super().__init__(brand, speed)
        self.doors = doors

    def honk(self):
        print('Honk! Honk!')


# Usage
car = Car("Toyota", 120, 4)
car.drive()  # Inherited from Vehicle
car.honk()
