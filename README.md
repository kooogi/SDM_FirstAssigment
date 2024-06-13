Sure! Here is a README file for your parking system project:

### README

# Parking System Project

This is a simple parking system implemented in Python. The system manages parking slots, handles vehicle information, calculates parking fees, and processes payments.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Classes](#classes)
  - [Parking](#parking)
  - [Vehicle](#vehicle)
  - [ParkingSlot](#parkingslot)
  - [PayAndDisplay](#payanddisplay)
- [Example](#example)

## Features

- Manage parking slots (assign and free slots).
- Track vehicle information (license plate, brand, model, owner).
- Calculate parking fees based on duration.
- Process payments and display receipts.

## Installation

1. Ensure you have Python 3 installed on your system.
2. Clone this repository or download the source code.

```sh
git clone <repository_url>
```

3. Navigate to the project directory.

```sh
cd <project_directory>
```

## Usage

Run the `main.py` file to start the parking system.

```sh
python main.py
```

Follow the on-screen prompts to park or remove vehicles.

## Classes

### Parking

Manages the parking slots and handles the vehicle parking and removal process.

- **Methods:**
  - `__init__(self, total_slots)`: Initializes the parking lot with the specified number of slots.
  - `find_free_slot(self)`: Finds and returns a free parking slot.
  - `park_vehicle(self, vehicle)`: Parks a vehicle in a free slot.
  - `remove_vehicle(self, slot_id)`: Removes a vehicle from the specified slot and calculates the fee.

### Vehicle

Stores information about a vehicle.

- **Methods:**
  - `__init__(self, license_plate, brand, model, owner)`: Initializes the vehicle with the specified details.
  - `__str__(self)`: Returns a string representation of the vehicle.

### ParkingSlot

Represents an individual parking slot.

- **Methods:**
  - `__init__(self, slot_id)`: Initializes the parking slot with the specified ID.
  - `park_vehicle(self, vehicle)`: Parks a vehicle in this slot.
  - `remove_vehicle(self)`: Removes the vehicle from this slot.

### PayAndDisplay

Handles fee calculation, payment processing, and receipt display.

- **Methods:**
  - `calculate_fee(self, duration)`: Calculates the parking fee based on the duration.
  - `process_payment(self, amount)`: Simulates payment processing.
  - `display_receipt(self, vehicle, slot_id, duration, fee)`: Displays the receipt with the vehicle details, slot ID, duration, and fee.

## Example

```sh
1. Park Vehicle
2. Remove Vehicle
3. Exit
Enter your choice: 1
Enter vehicle license plate: ABC123
Enter vehicle brand: Toyota
Enter vehicle model: Camry
Enter vehicle owner: John Doe
Vehicle Toyota Camry (ABC123) owned by John Doe parked at slot 0.

1. Park Vehicle
2. Remove Vehicle
3. Exit
Enter your choice: 2
Enter slot id to remove vehicle from: 0

--- Receipt ---
Vehicle: Toyota Camry (ABC123) owned by John Doe
Slot ID: 0
Duration: 0:01:20.123456
Fee: $0.02
----------------

Payment of $0.02 processed successfully.
Vehicle removed from slot 0.
```