from bus import Bus
from passenger import Passenger
from admin import Admin


class BusSystem:
    def __init__(self):
        self.buses = []
        self.passengers = []
        self.admin = Admin()

    def add_bus(self, number, route, seats):
        for bus in self.buses:
            if bus.number == number:
                print(f"\n[Error] Bus with number {number} already exists!")
                return
        new_bus = Bus(number, route, seats)
        self.buses.append(new_bus)
        print(f"\n[Success] Bus {number} added successfully!")

    def show_buses(self):
        if not self.buses:
            print("\nNo buses available in the system.")
            return

        print("\n--- Available Buses ---")
        for bus in self.buses:
            print(f"Bus No: {bus.number} | Route: {bus.route} | Available Seats: {bus.available_seats()}/{bus.total_seats}")

    def book_ticket(self, bus_number, name, phone):
        selected_bus = None
        for bus in self.buses:
            if bus.number == bus_number:
                selected_bus = bus
                break

        if not selected_bus:
            print(f"\n[Error] Bus number {bus_number} not found!")
            return

        if selected_bus.book_seat():
            passenger = Passenger(name, phone, selected_bus)
            self.passengers.append(passenger)
            print("\n================ Ticket Confirmation ================")
            print(f"Passenger Name : {name}")
            print(f"Phone Number   : {phone}")
            print(f"Bus Number     : {selected_bus.number}")
            print(f"Route          : {selected_bus.route}")
            print("Total Fare     : ৳500 (Fixed)")
            print("Status         : Confirmed")
            print("=====================================================")
        else:
            print(f"\n[Sorry] No seats available on Bus {bus_number}!")