class Vehicle:
    def __init__(self, license_plate, brand, model, owner):
        self.license_plate = license_plate
        self.brand = brand
        self.model = model
        self.owner = owner

    def __str__(self):
        return f"{self.brand} {self.model} ({self.license_plate}) owned by {self.owner}"