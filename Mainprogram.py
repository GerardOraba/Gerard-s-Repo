from Inherit import Car, Motorcycle

# Main Program
def main():
    car1 = Car("Toyota", 80)
    bike1 = Motorcycle("Yamaha", 60)
    
    vehicles = [car1, bike1]


    for vehicle in vehicles:
        vehicle.move()

    car1.set_speed(100)
    print("\nUpdated Speed:")
    car1.move()

if __name__ == "__main__":
    main()