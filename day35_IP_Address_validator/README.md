**README — IP Address Validator (Python)**
📌 **Project Overview**

The IP Address Validator is a Python program that checks whether a given IPv4 address is valid.
It uses regular expressions and string manipulation to verify both the format and value ranges (0–255 for each octet).

This type of validation is **important** for:

- Network configuration
- System administration
- Data validation before processing

**Features**

- Validate IPv4 addresses:
Checks if the input is in correct IPv4 format (X.X.X.X).

- Range check for each octet:
Ensures each section of the IP is between 0 and 255.

- Interactive user input:
Program keeps running until the user types exit.

- Error detection:
Invalid IPs are clearly flagged.

**Python Concepts Covered**

- Regular Expressions (re module)
- Using re.compile() to define an IPv4 format pattern.
- String Manipulation
- .split('.') to divide IP address into parts.
- User Input
- input() to get data from the user.
- Conditional Statements
- Validating each part of the IP address.
- Loops
- Continuous prompting until user quits.

**Tools and Modules**
- Python Built-in Functions (input(), print(), split(), int())
- re Module — Regular expressions for format validation.

**How It Works**

- Regex Pattern Definition
- Matches the IPv4 format: four numbers (1–3 digits each) separated by dots.
- Validation Function
- Checks regex match.
- Splits IP into four parts.
- Ensures each part is between 0 and 255.
- User Interaction
- Repeats until "exit" is entered.
- Prints whether the IP is valid or invalid.

**Example Run**
Enter an IP address to validate or type 'exit' to quit: 

192.171.63.48

192.171.63.48 is a valid IP address.



Enter an IP address to validate or type 'exit' to quit: 

267.45.221.90

267.45.221.90 is an invalid IP address.



Enter an IP address to validate or type 'exit' to quit:

exit

Program terminated.

**How to Run**
- Save the file as ip_validator.py.
- Run in terminal:
python ip_validator.py