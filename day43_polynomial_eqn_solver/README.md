**Polynomial Equation Solver in Python**
**Project Overview**

The Polynomial Equation Solver is an intermediate-level Python project designed to:

- Parse polynomial equations input by the user.

- Calculate the roots of the polynomial.

- Display the results in a clear, readable format.

This project demonstrates the use of:

- Loops – to iterate through polynomial terms and roots.

- Lists and tuples – to store and manipulate polynomial coefficients.

- Functions – for parsing polynomials, finding roots, and user interaction.

- Numpy – for numerical computation of polynomial roots.

- String manipulation – for processing input equations.

**Features**
1.  Parse Polynomial

- Converts user input (e.g., 3x^2 + 2x - 5) into a list of coefficients.

- Handles positive/negative signs and different powers of x.

2. Find Roots

- Uses numpy.roots() to calculate roots accurately.

- 3. Supports polynomials of any degree.

- Interactive CLI

- Command line interface allows continuous input.

- Users can solve multiple polynomials without restarting the program.

4. Readable Output

- Displays roots in a user-friendly format.

**How to Run**

1. Copy the code below into a Python file named polynomial_solver.py.

2. Install Numpy if not already installed:

pip install numpy

3. Run the program in VS Code or any Python IDE:

python polynomial_solver.py


4. Enter the polynomial equation as prompted.

5. View roots and continue solving more polynomials as needed.

**Example Output**
Polynomial Equation Solver

Enter a polynomial equation (e.g., 3x^2 + 2x - 5): x^2 - 2x + 1

The roots of the polynomial are: [1. 1.]

Do you want to solve another polynomial? (yes/no): yes

Enter a polynomial equation (e.g., 3x^2 + 2x - 5): x^2 + 2x + 1

The roots of the polynomial are: [-1. -1.]

Do you want to solve another polynomial? (yes/no): no

Exiting Polynomial Solver. Goodbye!
