#!/usr/bin/env python3
"""
Customer Management System (command-line)
Data storage: customers.txt
Each record is one line with tab-separated fields:
id<TAB>name<TAB>address<TAB>phone\n
"""

DELIM = "\t"
DATA_FILE = "customers.txt"


def read_lines():
    """Return all lines from DATA_FILE as a list. If file doesn't exist, return empty list."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        return []


def write_lines(lines):
    """Overwrite DATA_FILE with the given list of lines."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        f.writelines(lines)


def add_customer():
    """Add a new customer. Prevent duplicate IDs."""
    customer_id = input("Enter customer ID: ").strip()
    if not customer_id:
        print("ID cannot be empty.\n")
        return

    # check duplicate
    for line in read_lines():
        parts = line.rstrip("\n").split(DELIM)
        if parts and parts[0] == customer_id:
            print(f"ID '{customer_id}' already exists. Use update instead.\n")
            return

    name = input("Enter customer name: ").strip()
    address = input("Enter customer address: ").strip()
    phone = input("Enter customer phone number: ").strip()

    row = DELIM.join([customer_id, name, address, phone]) + "\n"
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(row)

    print("Record added successfully.\n")


def delete_customer():
    """Delete a record by ID."""
    customer_id = input("Enter customer ID to delete: ").strip()
    if not customer_id:
        print("ID cannot be empty.\n")
        return

    lines = read_lines()
    if not lines:
        print("No records to delete.\n")
        return

    new_lines = []
    found = False
    for line in lines:
        parts = line.rstrip("\n").split(DELIM)
        if parts and parts[0] == customer_id:
            found = True
            # skip this line (delete)
            continue
        new_lines.append(line)

    if found:
        write_lines(new_lines)
        print("Record deleted successfully.\n")
    else:
        print("No record found with that ID.\n")


def update_customer():
    """Update an existing customer by ID. Leave blank to keep current values."""
    customer_id = input("Enter customer ID to update: ").strip()
    if not customer_id:
        print("ID cannot be empty.\n")
        return

    lines = read_lines()
    if not lines:
        print("No records to update.\n")
        return

    new_lines = []
    found = False
    for line in lines:
        parts = line.rstrip("\n").split(DELIM)
        if parts and parts[0] == customer_id:
            found = True
            current_name = parts[1] if len(parts) > 1 else ""
            current_address = parts[2] if len(parts) > 2 else ""
            current_phone = parts[3] if len(parts) > 3 else ""

            print("Enter new details (press Enter to keep current value):")
            name = input(f"Enter new customer name [{current_name}]: ").strip()
            address = input(f"Enter new customer address [{current_address}]: ").strip()
            phone = input(f"Enter new customer phone number [{current_phone}]: ").strip()

            name = name if name else current_name
            address = address if address else current_address
            phone = phone if phone else current_phone

            new_row = DELIM.join([customer_id, name, address, phone]) + "\n"
            new_lines.append(new_row)
        else:
            new_lines.append(line)

    if found:
        write_lines(new_lines)
        print("Record updated successfully.\n")
    else:
        print("No record found with that ID.\n")


def search_customer():
    """Search for a customer by ID and display details."""
    customer_id = input("Enter customer ID to search: ").strip()
    if not customer_id:
        print("ID cannot be empty.\n")
        return

    for line in read_lines():
        parts = line.rstrip("\n").split(DELIM)
        if parts and parts[0] == customer_id:
            id_, name, address, phone = (parts + [""] * 4)[:4]
            print("\n--- Customer Found ---")
            print(f"ID:      {id_}")
            print(f"Name:    {name}")
            print(f"Address: {address}")
            print(f"Phone:   {phone}\n")
            return

    print("No record found with that ID.\n")


def show_all_customers():
    """Display all records in a simple table format."""
    lines = read_lines()
    print("\nID\tName\tAddress\tPhone")
    print("-" * 50)
    if not lines:
        print("No records found.\n")
        return
    for line in lines:
        # Each line already uses tabs; print it (strip trailing newline)
        print(line.rstrip("\n"))
    print()


def main_menu():
    """Main menu loop."""
    while True:
        print("Welcome to the Customer Portal")
        print("Options:")
        print("1. Add customer")
        print("2. Delete customer")
        print("3. Update customer")
        print("4. Search customer")
        print("5. Show all customers")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()
        if choice == "1":
            add_customer()
        elif choice == "2":
            delete_customer()
        elif choice == "3":
            update_customer()
        elif choice == "4":
            search_customer()
        elif choice == "5":
            show_all_customers()
        elif choice == "6":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 6.\n")


if __name__ == "__main__":
    main_menu()
