# Polymorphism
# Definition: Allows methods in different classes to have the same name but behave differently.
# Purpose: Enables flexibility and integration of classes with different implementations under a common interface.


class Bird:
    def sound(self):
        print("Chirp chirp")

class Dog:
    def sound(self):
        print("Bark bark")

def make_sound(animal):
    animal.sound()

# Usage
bird = Bird()
dog = Dog()
make_sound(bird)  # Chirp chirp
make_sound(dog)   # Bark bark
