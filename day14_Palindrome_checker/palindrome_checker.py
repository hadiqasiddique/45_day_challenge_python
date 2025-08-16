def main():
    while True:
        print("\n=== Palindrome Checker ===")
        print("1. Check a string")
        print("2. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if choice == 1:
            user_input = input("Enter a string to check: ")
            
            # Check if string is palindrome (case-insensitive, ignoring spaces)
            cleaned_input = user_input.replace(" ", "").lower()
            if cleaned_input == cleaned_input[::-1]:
                print(f"'{user_input}' is a palindrome.")
            else:
                print(f"'{user_input}' is NOT a palindrome.")
        
        elif choice == 2:
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
