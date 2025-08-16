# Inventory Tracker Application

# Step 1: Create inventory dictionary
inventory = {}

# Function to display inventory
def display_inventory():
    if not inventory:
        print("\nInventory is empty.")
    else:
        print("\nCurrent Inventory:")
        for item, quantity in inventory.items():
            print(f"{item} : {quantity}")

# Function to add item
def add_item():
    item = input("Enter item name: ").strip().lower()
    qty = int(input(f"Enter quantity for {item}: "))
    if item in inventory:
        inventory[item] += qty
        print(f"Updated {item}. New quantity: {inventory[item]}")
    else:
        inventory[item] = qty
        print(f"Added {item} with quantity {qty}")

# Function to remove item
def remove_item():
    item = input("Enter item name to remove: ").strip().lower()
    if item in inventory:
        del inventory[item]
        print(f"{item} removed from inventory.")
    else:
        print(f"{item} not found in inventory.")

# Function to update item quantity
def update_item():
    item = input("Enter item name to update: ").strip().lower()
    if item in inventory:
        qty = int(input(f"Enter new quantity for {item}: "))
        inventory[item] = qty
        print(f"{item} updated to quantity {qty}")
    else:
        print(f"{item} not found in inventory.")

# Function to search for an item
def search_item():
    item = input("Enter item name to search: ").strip().lower()
    if item in inventory:
        print(f"{item} is available with quantity {inventory[item]}")
    else:
        print(f"{item} is not available in inventory.")

# Step 3: Main menu
def main():
    while True:
        print("\n--- Inventory Tracker Menu ---")
        print("1. Display Inventory")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Update Item Quantity")
        print("5. Search Item")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            display_inventory()
        elif choice == "2":
            add_item()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            update_item()
        elif choice == "5":
            search_item()
        elif choice == "6":
            print("Exiting Inventory Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
