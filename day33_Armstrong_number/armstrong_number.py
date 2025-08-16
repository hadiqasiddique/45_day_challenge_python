def is_armstrong_number(number):
    """Check if a given number is an Armstrong number.
    An Armstrong number is equal to the sum of its digits each raised
    to the power of the number of digits."""
    num_str = str(number)
    num_length = len(num_str)
    sum_of_powers = sum(int(digit) ** num_length for digit in num_str)
    return number == sum_of_powers

def main():
    """Main function to run the Armstrong Number Checker."""
    while True:
        user_input = input("Enter a number to check if it is Armstrong (or Q to quit): ").strip()

        if user_input.lower() == 'q':
            print("Exiting program...")
            break

        try:
            num = int(user_input)
            if is_armstrong_number(num):
                print(f"{num} is an Armstrong number.")
            else:
                print(f"{num} is NOT an Armstrong number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
