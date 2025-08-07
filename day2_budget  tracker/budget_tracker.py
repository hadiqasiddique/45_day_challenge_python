def main():
    income = float(input("Enter your total income: "))
    expenses = {}

    while True:
        expense_name = input("Enter your expense name (or 'done' to finish): ")
        if expense_name.lower() == 'done':
            break
        expense_amount = float(input(f"Enter the amount for {expense_name}: "))
        expenses[expense_name] = expense_amount

    total_expenses = sum(expenses.values())
    surplus_or_deficit = income - total_expenses

    print("\nBudget Summary")
    print("--------------------------")
    print(f"Total Income: ${round(income, 2)}")
    print(f"Total Expenses: ${round(total_expenses, 2)}")

    print("\nExpenses Breakdown")
    for name, amount in expenses.items():
        print(f"{name}: ${round(amount, 2)}")

    print(f"\nSurplus/Deficit: ${round(surplus_or_deficit, 2)}")


if __name__ == "__main__":
    main()
