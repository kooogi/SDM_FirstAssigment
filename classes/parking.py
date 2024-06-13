 
import datetime
from classes.parkingSlot import ParkingSlot
from classes.payAndDisplay import PayAndDisplay


class Parking:
    def __init__(self, total_slots):
        self.total_slots = total_slots
        self.slots = [ParkingSlot(i) for i in range(total_slots)]
        self.pay_and_display = PayAndDisplay()

    def find_free_slot(self):
        for slot in self.slots:
            if not slot.is_occupied:
                return slot
        return None

    def park_vehicle(self, vehicle):
        slot = self.find_free_slot()
        if slot:
            slot.park_vehicle(vehicle)
            print(f"Vehicle {vehicle} parked at slot {slot.slot_id}.")
        else:
            print("No free slots available.")

    def remove_vehicle(self, slot_id):
        if 0 <= slot_id < self.total_slots:
            slot = self.slots[slot_id]
            if slot.is_occupied:
                current_time = datetime.datetime.now()
                duration = current_time - slot.entry_time
                fee = self.pay_and_display.calculate_fee(duration)
                
                self.pay_and_display.display_receipt(slot.vehicle, slot.slot_id, duration, fee)
                self.pay_and_display.process_payment(fee)
                
                slot.remove_vehicle()
                print(f"Vehicle removed from slot {slot_id}.")
            else:
                print("Slot is already empty.")
        else:
            print("Invalid slot id.")