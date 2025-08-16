import numpy as np

# Function to parse polynomial string into coefficients
def parse_polynomial(poly):
    terms = poly.replace('-', '+-').split('+')
    coefficients = []

    for term in terms:
        term = term.strip()
        if term == '':
            continue
        if 'x' in term:
            if '^' in term:
                coef, power = term.split('x^')
                if coef == '' or coef == '+':
                    coef = 1
                elif coef == '-':
                    coef = -1
                coefficients.append((int(coef), int(power)))
            else:
                coef = term.split('x')[0]
                if coef == '' or coef == '+':
                    coef = 1
                elif coef == '-':
                    coef = -1
                coefficients.append((int(coef), 1))
        else:
            coefficients.append((int(term), 0))

    degree = max(power for _, power in coefficients)
    poly_list = [0] * (degree + 1)
    for coef, power in coefficients:
        poly_list[degree - power] = coef

    return poly_list

# Function to find roots of the polynomial
def find_roots(coefficients):
    roots = np.roots(coefficients)
    return roots

# Main function to handle CLI
def main():
    print("Polynomial Equation Solver")
    while True:
        poly_string = input("Enter a polynomial equation (e.g., 3x^2 + 2x - 5): ")
        coefficients = parse_polynomial(poly_string)
        roots = find_roots(coefficients)
        print(f"The roots of the polynomial are: {roots}")

        cont = input("Do you want to solve another polynomial? (yes/no): ").lower()
        if cont == 'yes':
            continue
        elif cont == 'no':
            print("Exiting Polynomial Solver. Goodbye!")
            break
        else:
            print("Invalid choice. Exiting.")
            break

if __name__ == "__main__":
    main()
