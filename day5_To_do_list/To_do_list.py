# To-Do List Application

# Step 1: Create lists
todo_list = []
completed_list = []

# Add new item
def add_item():
    item = input("Enter the item to add: ")
    todo_list.append(item)
    print(f'"{item}" has been added to the To-Do list.\n')

# Remove item
def remove_item():
    index = input("Enter the index of the item to remove: ")
    if index.isdigit() and 1 <= int(index) <= len(todo_list):
        removed_item = todo_list.pop(int(index) - 1)
        print(f'"{removed_item}" has been removed from the To-Do list.\n')
    else:
        print("Invalid index. Please try again.\n")

# Display list
def display_list(lst, list_name):
    print(f"\n{list_name}:")
    if not lst:
        print("No items.\n")
        return
    for index, item in enumerate(lst, start=1):
        print(f"{index}. {item}")
    print()

# Mark item as completed
def mark_item_completed():
    index = input("Enter the index of the item to mark as completed: ")
    if index.isdigit() and 1 <= int(index) <= len(todo_list):
        completed_item = todo_list.pop(int(index) - 1)
        completed_list.append(completed_item)
        print(f'"{completed_item}" has been marked as completed.\n')
    else:
        print("Invalid index. Please try again.\n")

# Main menu
def main():
    while True:
        print("\n=== TO-DO LIST ===")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Mark Item as Completed")
        print("4. Display To-Do List")
        print("5. Display Completed List")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            mark_item_completed()
        elif choice == "4":
            display_list(todo_list, "To-Do List")
        elif choice == "5":
            display_list(completed_list, "Completed List")
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
