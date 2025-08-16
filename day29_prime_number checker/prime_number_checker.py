import math

def is_prime(number):
    """Check if a number is prime."""
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def main():
    """Main function to run the prime number checker."""
    while True:
        user_input = input("Enter a number (or Q to quit): ").strip()
        
        if user_input.lower() == "q":
            print("Exiting...")
            break

        try:
            num = int(user_input)
            if is_prime(num):
                print(f"{num} is prime.")
            else:
                print(f"{num} is not prime.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        again = input("Do you want to check another number? (yes/no): ").strip().lower()
        if again != "yes":
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
