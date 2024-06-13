class PayAndDisplay:
    def calculate_fee(self, duration):
        hours = duration.total_seconds() / 3600
        return hours * 1

    def process_payment(self, amount):
        print(f"Payment of ${amount:.2f} processed successfully.")

    def display_receipt(self, vehicle, slot_id, duration, fee):
        print("\n--- Receipt ---")
        print(f"Vehicle: {vehicle}")
        print(f"Slot ID: {slot_id}")
        print(f"Duration: {duration}")
        print(f"Fee: ${fee:.2f}")
        print("----------------\n")
