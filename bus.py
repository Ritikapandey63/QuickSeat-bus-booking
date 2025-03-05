import sys

# Sample data for buses and routes
buses = {
    101: {"route": "City A to City B", "seats": 30, "price": 100},
    102: {"route": "City B to City C", "seats": 25, "price": 120},
    103: {"route": "City A to City C", "seats": 20, "price": 150}
}

users = {}

# Function to display available buses
def show_buses():
    print("\nAvailable Buses:")
    for bus_id, bus_info in buses.items():
        print(f"Bus ID: {bus_id}, Route: {bus_info['route']}, Available Seats: {bus_info['seats']}, Price: {bus_info['price']}")

# Function to register a user
def register_user():
    username = input("Enter your username: ")
    if username in users:
        print("Username already exists. Please login.")
        return None
    password = input("Enter your password: ")
    users[username] = {"password": password, "bookings": []}
    print(f"User {username} registered successfully.")
    return username

# Function to login a user
def login_user():
    username = input("Enter your username: ")
    if username not in users:
        print("Username not found. Please register first.")
        return None
    password = input("Enter your password: ")
    if users[username]["password"] == password:
        print(f"Welcome back, {username}!")
        return username
    else:
        print("Incorrect password. Please try again.")
        return None

# Function to book a ticket
def book_ticket(username):
    show_buses()
    bus_id = int(input("Enter Bus ID to book: "))
    if bus_id not in buses:
        print("Invalid Bus ID. Please try again.")
        return

    bus = buses[bus_id]
    if bus["seats"] > 0:
        bus["seats"] -= 1
        ticket = {"bus_id": bus_id, "route": bus["route"], "price": bus["price"]}
        users[username]["bookings"].append(ticket)
        print(f"Ticket booked successfully! Route: {bus['route']}, Price: {bus['price']}")
    else:
        print("Sorry, no seats available on this bus.")

# Function to view user's bookings
def view_bookings(username):
    if not users[username]["bookings"]:
        print("No bookings found.")
        return
    print("\nYour Bookings:")
    for booking in users[username]["bookings"]:
        print(f"Route: {booking['route']}, Price: {booking['price']}")

# Main Menu
def main():
    print("Welcome to the Bus Booking System")
    
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            username = register_user()
            if username:
                user_dashboard(username)
        elif choice == '2':
            username = login_user()
            if username:
                user_dashboard(username)
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

# User dashboard after login/registration
def user_dashboard(username):
    while True:
        print("\n1. Book Ticket\n2. View Bookings\n3. Logout")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            book_ticket(username)
        elif choice == '2':
            view_bookings(username)
        elif choice == '3':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the system
if __name__ == "__main__":
    main()
