from oop import Vehicle

# Inheritance
class Car(Vehicle):
    def move(self):
        print(f"{self.brand} Car is moving at {self.get_speed()} km/h")

class Motorcycle(Vehicle):
    def move(self):
        print(f"{self.brand} Motorycycle is moving at {self.get_speed()} km/h ")
