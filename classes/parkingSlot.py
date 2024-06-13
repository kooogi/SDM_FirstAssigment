import datetime


class ParkingSlot:
    def __init__(self, slot_id):
        self.slot_id = slot_id
        self.is_occupied = False
        self.vehicle = None
        self.entry_time = None

    def park_vehicle(self, vehicle):
        self.is_occupied = True
        self.vehicle = vehicle
        self.entry_time = datetime.datetime.now()

    def remove_vehicle(self):
        self.is_occupied = False
        self.vehicle = None
        self.entry_time = None