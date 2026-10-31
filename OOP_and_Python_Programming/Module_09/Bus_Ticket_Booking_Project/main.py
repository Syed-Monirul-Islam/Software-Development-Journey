from bus_system import BusSystem

system = BusSystem()


system.add_bus("B-101", "Dhaka to Chattogram", 40)
system.add_bus("B-102", "Dhaka to Sylhet", 30)

while True:
    print("\n===== Bangladesh Bus Ticket Booking System =====")
    print("1. Admin Login")
    print("2. Book Ticket")
    print("3. View Buses")
    print("4. Exit")

    choice = input("Enter choice (1-4): ").strip()

    if choice == "1":
        print("\n--- Admin Login ---")
        user = input("Username: ").strip()
        pwd = input("Password: ").strip()

        if system.admin.login(user, pwd):
            print("\n[Login Successful] Welcome Admin!")
            while True:
                print("\n--- Admin Menu ---")
                print("1. Add Bus")
                print("2. View All Buses")
                print("3. Logout")
                admin_choice = input("Enter choice (1-3): ").strip()

                if admin_choice == "1":
                    num = input("Enter Bus Number: ").strip()
                    route = input("Enter Route: ").strip()
                    seats_in = input("Enter Total Seats: ").strip()

                    if seats_in.isdigit() and int(seats_in) > 0:
                        system.add_bus(num, route, int(seats_in))
                    else:
                        print("\n[Error] Seats must be a valid positive number.")
                elif admin_choice == "2":
                    system.show_buses()
                elif admin_choice == "3":
                    print("\nLogged out successfully.")
                    break
                else:
                    print("\n[Invalid Option] Please enter 1, 2, or 3.")
        else:
            print("\n[Error] Invalid Username or Password!")

    elif choice == "2":
        print("\n--- Book Ticket ---")
        system.show_buses()
        bus_no = input("\nEnter Bus Number to book: ").strip()
        name = input("Enter Passenger Name: ").strip()
        phone = input("Enter Phone Number: ").strip()

        if bus_no and name and phone:
            system.book_ticket(bus_no, name, phone)
        else:
            print("\n[Error] All fields are required.")

    elif choice == "3":
        system.show_buses()

    elif choice == "4":
        print("\nThank you for using Bangladesh Bus Ticket Booking System. Goodbye!")
        break

    else:
        print("\n[Invalid Option] Please enter a valid number (1-4).")