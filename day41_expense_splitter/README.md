**Expense Splitter Python Project**
📌Project Overview

The **Expense Splitter** is a Python program designed to help groups of people split shared expenses fairly. The program allows users to:

- Add expenses with payer name, amount, and description

- View a summary of all expenses

- Calculate and display the balances showing who owes or should receive money

This project demonstrates the use of:

- User-defined functions

- Lists and dictionaries

- Conditional statements (if, elif, else)

- Loops (for, while)

- f-string formatting

- Basic input/output operations in Python

- No external libraries are required; this project is fully based on Python’s core features.

**Features**

1. Add Expense

-  Users can add a new expense with:

-  Name of the payer

- Amount paid

- expense description

- Expenses are stored in a list of dictionaries.

- 7Total amount paid by each payer is stored in a dictionary.

2. Calculate Splits

- Total amount of all expenses is calculated.

- Amount each person should pay is calculated based on equal split.

- Balances are computed showing how much each payer owes or should receive.

3. View Summary

- Displays a detailed list of all expenses: payer, amount, description.

- Displays final balances:

- Positive balance → person should receive money

- Negative balance → person owes money

- Zero balance → settled

4. Main Menu

- Infinite loop menu with options:

- Add Expense

- View Summary

5. Exit

**How to Run**

- Copy the code below into a Python file (e.g., expense_splitter.py).

- Run the program in VS Code or any Python IDE.

- Follow the prompts in the console to add expenses and view summaries.


**Example Output**

--- Expense Splitter Menu ---
1. Add Expense
2. View Summary
3. Exit

Enter your choice: 1

Enter your name: Alice

Enter amount: 50

Enter description: Groceries

Expense 'Groceries' added: $50 by Alice


Enter your choice: 1

Enter your name: Bob

Enter amount: 30

Enter description: Food Bill

Expense 'Food Bill' added: $30 by Bob


Enter your choice: 2

Expenses Summary:

Payer: Alice, Amount: $50, Description: Groceries

Payer: Bob, Amount: $30, Description: Food Bill

Final Balances:

Alice should receive $10.00

Bob owes $10.00


Enter your choice: 3
Exiting Expense Splitter. Goodbye!
