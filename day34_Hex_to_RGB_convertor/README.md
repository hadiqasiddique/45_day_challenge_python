📄 **README — Hex to RGB Converter (Python)**
📌 **Project Overview**

The Hex to RGB Converter is a Python program that converts hexadecimal color codes (used in HTML, CSS, and other applications) into RGB values.
RGB stands for Red, Green, and Blue, and each color component ranges from 0 to 255.

**project demonstrates:**

- String manipulation

- Converting hexadecimal to decimal

- User input handling and validation

- Exception handling in Python

**Features**

- Convert Hex to RGB: Converts valid 6-character hex codes to RGB values.

- User Input: Allows users to input hex codes manually.

- Error Handling: Detects and reports invalid hex codes.

- Exit Option: Lets users quit by typing "exit".

**Python Concepts Covered**

- String Manipulation
- Using .lstrip() to remove the # symbol.
- Slicing strings to extract R, G, and B components.
- Hexadecimal to Decimal Conversion
- Using int(value, 16) to convert hex to decimal.
- User Input and Validation
- Accepting input via input().
- Validating length and format using try/except.
- Exception Handling
- Raising ValueError for incorrect input.

**Tools and Modules**

- Python Built-in Functions Only (No external libraries required)

**How It Works**

- Hex to RGB Function
- Removes # if present.
- Checks if the hex code is exactly 6 characters.
- Converts each pair of hex characters to decimal (R, G, B).
- User Interaction
- Prompts the user for a hex code.
--Allows "exit" to quit.
- Error Handling
- Handles invalid formats and wrong lengths gracefully.

**Example Run**
Hex to RGB Conversion

Enter a hex code or type 'exit' to quit: FFFFFF
RGB Value: (255, 255, 255)

Enter a hex code or type 'exit' to quit: #FF5733
RGB Value: (255, 87, 51)

Enter a hex code or type 'exit' to quit: exit
Program terminated.

**How to Run**

- Save the code as hex_to_rgb.py.

- Open a terminal and run:
python hex_to_rgb.py