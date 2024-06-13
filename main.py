from classes.parking import Parking
from classes.vehicle import Vehicle



def main():
    parking_lot = Parking(10)

    while True:
        print("\n1. Park Vehicle\n2. Remove Vehicle\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            license_plate = input("Enter vehicle license plate: ")
            brand = input("Enter vehicle brand: ")
            model = input("Enter vehicle model: ")
            owner = input("Enter vehicle owner: ")
            vehicle = Vehicle( license_plate, brand, model, owner)
            parking_lot.park_vehicle(vehicle)
        elif choice == '2':
            slot_id = int(input("Enter slot id to remove vehicle from: "))
            parking_lot.remove_vehicle(slot_id)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
