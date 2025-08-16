# Expense Splitter Python Project
# Function to add an expense
def add_expense(expenses, payers):
    payer = input("Enter your name: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    # Append expense as dictionary to the list
    expenses.append({
        "payer": payer,
        "amount": amount,
        "description": description
    })

    # Update total paid by each payer
    if payer not in payers:
        payers[payer] = 0
    payers[payer] += amount

    print(f"Expense '{description}' added: ${amount} by {payer}")

# Function to calculate splits and balances
def calculate_splits(expenses, payers):
    total_amount = sum(expense["amount"] for expense in expenses)
    split_amount = total_amount / len(payers)

    balances = {payer: 0 for payer in payers}
    for payer in balances:
        balances[payer] = payers[payer] - split_amount

    return balances

# Function to view summary
def view_summary(expenses, payers):
    if not expenses:
        print("No expenses recorded.")
    else:
        print("\nExpenses Summary:\n")
        for expense in expenses:
            print(f"Payer: {expense['payer']}, Amount: ${expense['amount']}, Description: {expense['description']}")

        balances = calculate_splits(expenses, payers)
        print("\nFinal Balances:\n")
        for payer, balance in balances.items():
            if balance > 0:
                print(f"{payer} should receive ${balance:.2f}")
            elif balance < 0:
                print(f"{payer} owes ${-balance:.2f}")
            else:
                print(f"{payer} is settled")

# Main function
def main():
    expenses = []  # List to store all expenses
    payers = {}    # Dictionary to store total paid by each payer

    while True:
        print("\n--- Expense Splitter Menu ---")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_expense(expenses, payers)
        elif choice == 2:
            view_summary(expenses, payers)
        elif choice == 3:
            print("Exiting Expense Splitter. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
