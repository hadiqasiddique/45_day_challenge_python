# Python Tip Calculator

def calculate_tip(bill_amount, tip_percentage):
    """Calculate tip based on bill amount and tip percentage."""
    return bill_amount * (tip_percentage / 100)

def main():
    print("=== Welcome to Tip Calculator ===")
    
    try:
        # Take user input
        bill_amount = float(input("Enter your bill amount ($): "))
        tip_percentage = float(input("Enter tip percentage (%): "))
        
        # Calculate tip
        tip_amount = calculate_tip(bill_amount, tip_percentage)
        
        # Calculate total amount
        total_amount = bill_amount + tip_amount
        
        # Display results
        print(f"\nBill Amount: ${bill_amount:.2f}")
        print(f"Tip Percentage: {tip_percentage}%")
        print(f"Tip Amount: ${tip_amount:.2f}")
        print(f"Total Bill Amount: ${total_amount:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

# Call main function
if __name__ == "__main__":
    main()
