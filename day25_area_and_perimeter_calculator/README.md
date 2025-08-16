**README — Area and Perimeter Calculator**
📌 **Project Overview**

The Area and Perimeter Calculator is a Python program that computes the area and perimeter (or circumference) of four common 2D shapes:

1. Rectangle

2. Square

3. Circle

4. Triangle

By the end of this project, you'll learn:

- How to use functions to structure your code.

- How to use math formulas in Python.

- How to handle user input interactively.

🔹 **Features**

Supports 4 shapes: Rectangle, Square, Circle, Triangle.

- Calculates both area and perimeter (or circumference for circles).

- Uses Heron’s formula for triangle area.

- Fully menu-driven interface for easy user interaction.

- Validates choices and handles exit gracefully.

📚 **Python Concepts Used**

- Functions (8 functions: area & perimeter for each shape)

- Conditional statements (if, elif, else)

- Loops (while True loop for menu)

- Math module (math.pi & math.sqrt)

- User input handling (input() & float())

🛠 **Tools & Modules**

- math module for mathematical constants & functions.

- Built-in functions: input(), print().

📝 **Formulas Used**

**Formulas**

**Rectangle**

Area: length * width

Perimeter: 2 * (length + width)

**Square**

Area: side ** 2

Perimeter: 4 * side

**Circle**

Area: math.pi * radius ** 2

Circumference: 2 * math.pi * radius

**Triangle** (Heron’s Formula)

s = (a + b + c) / 2

Area: math.sqrt(s * (s - a) * (s - b) * (s - c))

Perimeter: a + b + c

🚀**How It Works**

- Displays a menu for shape selection.

- User selects a shape and enters required dimensions.

- Program calculates and displays area and perimeter.

- Continues until the user selects Exit.

**Requirements**

- Python 3.8 or newer

- Standard library only (uses math)

**How to Run**

- Save the script as area_perimeter_calculator.py.

- Open a terminal in that folder.

- Run:
Windows: python area_perimeter_calculator.py

**Usage**

1. Choose a shape from the menu.

2. Enter the requested dimensions.

3. Program prints area and perimeter, then returns to the menu.

4. Choose option 5 to exit.

**Example Session**
Area and Perimeter Calculator
------------------------------
1. Rectangle
2. Square
3. Circle
4. Triangle
5. Exit

Enter your choice: 1

Enter the length: 3.4

Enter the width: 2.1

Area: 7.14

Perimeter: 11.0