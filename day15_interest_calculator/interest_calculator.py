# Interest Calculator in Python

# Function to calculate Simple Interest
def calculate_simple_interest(principal, rate, time):
    """ Calculate simple interest Formula: (Principal * Rate * Time) / 100"""
    return (principal * rate * time) / 100

# Function to calculate Compound Interest
def calculate_compound_interest(principal, rate, time, n=1):
    """
    Calculate compound interest
    Formula: Principal * (1 + Rate/(n*100))^(n*Time) - Principal
    n = number of times interest is compounded per year (default=1)
    """
    return principal * ((1 + rate / (n * 100)) ** (n * time)) - principal

# Main function
def main():
    print("Interest Calculator\n")

    # Taking user input
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time in years: "))

    # Calculating simple and compound interest
    simple_interest = calculate_simple_interest(principal, rate, time)
    compound_interest = calculate_compound_interest(principal, rate, time)

    # Displaying results
    print(f"\nSimple Interest = {simple_interest}")
    print(f"Compound Interest = {compound_interest}")

# Calling main function
if __name__ == "__main__":
    main()
