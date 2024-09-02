# Initialize parking spots
spots = {"A1": None, "A2": None, "A3": None, "B1": None, "B2": None, "B3": None}

# Define function to show available parking spots
def show_available_spots():
    print("Available spots:")
    for spot, car in spots.items():
        if car is None:
            print(spot)

# Define function to park a car
def park_car(spot, car):
    if spot in spots:
        if spots[spot] is None:
            spots[spot] = car
            print(f"{car} has been parked at {spot}.")
        else:
            print(f"{spot} is already occupied.")
    else:
        print("Invalid spot.")

# Define function to remove a car
def remove_car(spot):
    if spot in spots:
        if spots[spot] is not None:
            car = spots[spot]
            spots[spot] = None
            print(f"{car} has been removed from {spot}.")
        else:
            print(f"{spot} is already empty.")
    else:
        print("Invalid spot.")

# Main loop
while True:
    # Display menu
    print("\nWhat do you want to do?")
    print("1. Show available spots")
    print("2. Park a car")
    print("3. Remove a car")
    print("4. Quit")
    
    # Get user input
    choice = input("> ")
    
    # Process user input
    if choice == "1":
        show_available_spots()
    elif choice == "2":
        spot = input("Enter the spot: ")
        car = input("Enter the car's registration number: ")
        park_car(spot, car)
    elif choice == "3":
        spot = input("Enter the spot: ")
        remove_car(spot)
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
