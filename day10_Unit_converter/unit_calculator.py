def inches_to_centimeters(inches):
    """Convert inches to centimeters."""
    return inches * 2.54

def centimeters_to_inches(cm):
    """Convert centimeters to inches."""
    return cm / 2.54

def pounds_to_kilograms(pounds):
    """Convert pounds to kilograms."""
    return pounds * 0.453592

def kilograms_to_pounds(kg):
    """Convert kilograms to pounds."""
    return kg / 0.453592

def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5.0 / 9.0

def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return (c * 9.0 / 5.0) + 32

def unit_converter():
    """Main menu for the unit converter program."""
    print("\n=== UNIT CONVERTER ===")
    print("1. Length Conversion")
    print("2. Weight Conversion")
    print("3. Temperature Conversion")

    try:
        choice = int(input("\nEnter your choice (1/2/3): ").strip())
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if choice == 1:
        print("\n-- Length Conversion --")
        print("A. Inches → Centimeters")
        print("B. Centimeters → Inches")
        sub_choice = input("Enter your choice (A/B): ").strip().upper()

        if sub_choice == "A":
            try:
                inches = float(input("Enter value in inches: "))
                print(f"{inches} inches = {inches_to_centimeters(inches):.4f} cm")
            except ValueError:
                print("Invalid number entered.")
        elif sub_choice == "B":
            try:
                cm = float(input("Enter value in centimeters: "))
                print(f"{cm} cm = {centimeters_to_inches(cm):.4f} inches")
            except ValueError:
                print("Invalid number entered.")
        else:
            print("Invalid choice.")

    elif choice == 2:
        print("\n-- Weight Conversion --")
        print("A. Pounds → Kilograms")
        print("B. Kilograms → Pounds")
        sub_choice = input("Enter your choice (A/B): ").strip().upper()

        if sub_choice == "A":
            try:
                pounds = float(input("Enter value in pounds: "))
                print(f"{pounds} lbs = {pounds_to_kilograms(pounds):.4f} kg")
            except ValueError:
                print("Invalid number entered.")
        elif sub_choice == "B":
            try:
                kg = float(input("Enter value in kilograms: "))
                print(f"{kg} kg = {kilograms_to_pounds(kg):.4f} lbs")
            except ValueError:
                print("Invalid number entered.")
        else:
            print("Invalid choice.")

    elif choice == 3:
        print("\n-- Temperature Conversion --")
        print("A. Fahrenheit → Celsius")
        print("B. Celsius → Fahrenheit")
        sub_choice = input("Enter your choice (A/B): ").strip().upper()

        if sub_choice == "A":
            try:
                f = float(input("Enter value in Fahrenheit: "))
                print(f"{f}°F = {fahrenheit_to_celsius(f):.2f}°C")
            except ValueError:
                print("Invalid number entered.")
        elif sub_choice == "B":
            try:
                c = float(input("Enter value in Celsius: "))
                print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")
            except ValueError:
                print("Invalid number entered.")
        else:
            print("Invalid choice.")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    unit_converter()
