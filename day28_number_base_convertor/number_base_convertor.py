def decimal_to_binary(decimal_number: int) -> str:
    """Convert decimal (base 10) to binary (base 2)."""
    return bin(decimal_number)[2:]

def decimal_to_hexadecimal(decimal_number: int) -> str:
    """Convert decimal (base 10) to hexadecimal (base 16)."""
    return hex(decimal_number)[2:].upper()

def binary_to_decimal(binary_number: str) -> int:
    """Convert binary (base 2) string to decimal (base 10)."""
    return int(binary_number, 2)

def hexadecimal_to_decimal(hexadecimal_number: str) -> int:
    """Convert hexadecimal (base 16) string to decimal (base 10)."""
    return int(hexadecimal_number, 16)

def main():
    while True:
        print("\n=== Number Base Converter ===")
        print("1. Decimal to Binary")
        print("2. Decimal to Hexadecimal")
        print("3. Binary to Decimal")
        print("4. Hexadecimal to Decimal")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1–5.")
            continue

        if choice == 1:
            try:
                decimal_number = int(input("Enter a decimal number: "))
                print(f"Binary: {decimal_to_binary(decimal_number)}")
            except ValueError:
                print("Invalid input. Please enter a valid decimal number.")

        elif choice == 2:
            try:
                decimal_number = int(input("Enter a decimal number: "))
                print(f"Hexadecimal: {decimal_to_hexadecimal(decimal_number)}")
            except ValueError:
                print("Invalid input. Please enter a valid decimal number.")

        elif choice == 3:
            binary_number = input("Enter a binary number: ")
            try:
                print(f"Decimal: {binary_to_decimal(binary_number)}")
            except ValueError:
                print("Invalid binary number. Please use only 0s and 1s.")

        elif choice == 4:
            hexadecimal_number = input("Enter a hexadecimal number: ")
            try:
                print(f"Decimal: {hexadecimal_to_decimal(hexadecimal_number)}")
            except ValueError:
                print("Invalid hexadecimal number. Use digits 0–9 and letters A–F.")

        elif choice == 5:
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1–5.")


if __name__ == "__main__":
    main()
