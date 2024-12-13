# Abstraction
# Definition: Exposing only essential details and hiding the implementation. 
#             Python uses abstract classes via the abc module to enforce abstraction.
# Example: A Shape class defines methods like area, but specific shapes (e.g., Rectangle) implement the details.

#        	            Abstract Method	                            Normal Method
# Implementation	    No implementation in the base class	        Full implementation in the base class
# Purpose	            Enforces implementation in subclasses	    Provides default behavior or functionality
# Usage in Subclass	    Must be overridden	                        Can be overridden (optional)
# Instance Creation	    Cannot create an instance of the base class	Can create an instance of the class


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Usage
circle = Circle(5)
rect = Rectangle(4, 6)
print("Circle area:", circle.area())  # 78.5
print("Rectangle area:", rect.area())  # 24
