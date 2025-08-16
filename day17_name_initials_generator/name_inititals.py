def generate_initials(full_name):
    # Remove leading/trailing spaces and split into words
    name_parts = full_name.strip().split()
    # Get the first character of each word, make it uppercase
    initials = ''.join([part[0].upper() for part in name_parts])
    return initials

def main():
    while True:
        print("\n==== Name Initials Generator ====")
        print("1. Generate Initials")
        print("2. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        if choice == 1:
            full_name = input("Enter your full name: ")
            initials = generate_initials(full_name)
            print(f"The initials are: {initials}")
        elif choice == 2:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
