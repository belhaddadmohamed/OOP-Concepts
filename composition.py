# What is Composition in OOP?

# Definition: Composition is a design principle where one class contains an instance of another class as a part of its attributes.
# It represents a "has-a" relationship rather than an "is-a" relationship (which is inheritance).
# For example, a Car has-a Engine.

# Purpose:
# Composition allows us to build complex objects by combining simpler objects.
# It promotes reusability and modularity because each component can function independently.


class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return "Engine started!"

    def stop(self):
        return "Engine stopped."

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  # Composition: Car "has-a" Engine

    def start_car(self):
        print(f"{self.brand} car is starting...")
        print(self.engine.start())  # Using the Engine's method

    def stop_car(self):
        print(f"{self.brand} car is stopping...")
        print(self.engine.stop())

# Usage
engine = Engine(200)  # Create an Engine object
car = Car("Tesla", engine)  # Pass the Engine object to the Car

car.start_car()
car.stop_car()
