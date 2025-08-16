Interest Calculator in Python
Overview

The Interest Calculator is a Python program that calculates Simple Interest and Compound Interest based on user inputs. It allows you to compare both types of interest, helping you understand how interest grows over time.

Features

✅ Calculate Simple Interest

✅ Calculate Compound Interest with default or custom compounding frequency

✅ Compare Simple vs Compound Interest side by side

✅ Interactive user input for Principal, Rate, and Time

✅ Clear, accurate output

**Python Concepts Covered**

Functions: User-defined functions for interest calculations

Arithmetic Operators: *, /, ** for calculations

User Input: Using input() and converting to float

Conditional Execution: if __name__ == "__main__":

**How It Works**

1-Define Functions:

calculate_simple_interest(principal, rate, time)

Formula:
Simple Interest = (Principal × Rate × Time) / 100

calculate_compound_interest(principal, rate, time, n=1)

Formula:
Compound Interest = Principal * (1 + Rate/(n*100))^(n*Time) - Principal

2-Take User Input: Principal, rate, and time.

3-Calculate Interests: Call the functions with the user input.

4-Display Results: Show both simple and compound interest.

**Example**
Interest Calculator
Enter the principal amount: 1500.50
Enter the rate of interest: 3.5
Enter the time in years: 3

Simple Interest = 157.5525
Compound Interest = 163.13117

**How to Run**

Install Python 3.8+

Clone or download this repository

Open terminal in the project folder

Run the program:
python interest_calculator.py


