

totalbill = 0
def cj():
    global totalbill
    qty = int(input("Quantity: "))
    totalbill += qty * 95
    print(f"{qty} Chickenjoy added. ")

def jsp():
    global totalbill
    qty = int(input("Quantity: "))
    totalbill += qty * 60
    print(f"{qty} Jolly Spaghetti added. ")

def bs():
    global totalbill
    qty = int(input("Quantity:  "))
    totalbill += qty * 75
    print(f"{qty} Burger Steak added.  ")

def yb():
    global totalbill
    qty = int(input("Quantity: "))
    totalbill += qty * 50
    print(f"{qty} Yum Burger added. ")

def pmp():
    global totalbill
    qty = int(input("Quantity: "))
    totalbill += qty * 45
    print(f"{qty} Peach Mango Pie added. ")

def ViewTotal():
    global totalbill
    print(f"Total Bill: ₱{totalbill}")

while True:

    print("\n===========================================")
    print("         JOLLIBEE ORDERING SYSTEM            ")
    print("===========================================")
    print("1. Chickenjoy             - ₱95")
    print("2. Jolly Spaghetti        - ₱60")
    print("3. Burger Steak           - ₱75")
    print("4. Yum Burger             - ₱50")
    print("5. Peach Mango Pie        - ₱45")
    print("6. View Total Bill")
    print("7. Exit")
    print("===========================================")




    try:

        choice = int(input("Enter your choice: "))
    

        if choice == 1:
            cj()
        elif choice == 2:
            jsp()
        elif choice == 3:
            bs()
        elif choice == 4:
            yb()
        elif choice == 5:
            pmp()
        elif choice == 6:
            ViewTotal()
        elif choice == 7:
            print("Total amount is ₱",totalbill)
            print("Salamat gwapo")
            print("mwamwa")
            break

        else:
            print("Invalid choice. Choose 1-7 only")
    

    except ValueError:
        print("Invalid choice. Choose 1-7 only")
