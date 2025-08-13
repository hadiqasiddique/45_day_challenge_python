#!/usr/bin/env python3
import matplotlib.pyplot as plt

def main():
    # Initialize the expenses dictionary
    expenses = {}

    # Take input for expenses
    while True:
        expense_name = input("Enter the name of the expense (or 'done' to finish): ").strip()
        if expense_name.lower() == "done":
            break
        expense_amount = float(input(f"Enter the amount for {expense_name}: "))
        expenses[expense_name] = expense_amount

    # Call the plot function
    plot_expenses(expenses)

def plot_expenses(expenses):
    # Convert keys and values of dictionary into lists
    labels = list(expenses.keys())
    values = list(expenses.values())

    # Set figure size
    plt.figure(figsize=(7, 7))

    # Create the pie chart
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)

    # Equal aspect ratio ensures the pie is drawn as a circle
    plt.axis('equal')

    # Set title
    plt.title("Expense Breakdown")

    # Display the chart
    plt.show()

if __name__ == "__main__":
    main()