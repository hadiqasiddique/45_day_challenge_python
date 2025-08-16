import math

def calculate_gcd(a, b):
    """Return the Greatest Common Divisor of a and b."""
    return math.gcd(a, b)

def calculate_lcm(a, b):
    """Return the Least Common Multiple of a and b."""
    return abs(a * b) // math.gcd(a, b)

def main():
    print("\n=== GCD and LCM Calculator ===")
    
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
        gcd_result = calculate_gcd(num1, num2)
        lcm_result = calculate_lcm(num1, num2)
        
        print(f"The GCD of {num1} and {num2} is: {gcd_result}")
        print(f"The LCM of {num1} and {num2} is: {lcm_result}")
    
    except ValueError:
        print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()
