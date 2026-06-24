from abc import ABC, abstractmethod

# abstract Class (Abstraction)
class Vehicle(ABC):
    def __init__(self, brand, speed):
        self.brand = brand
        self._speed = speed # Encapsulation (Private Attribute)
    
    # Getter Method
    def get_speed(self):
        return self._speed
    
    def set_speed(self, speed):
        if speed >= 0:
            self._speed = speed

    @abstractmethod
    def move(self):
        pass