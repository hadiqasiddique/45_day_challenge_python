import math
# Rectangle
def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)

# Square
def square_area(side):
    return side ** 2

def square_perimeter(side):
    return 4 * side

# Circle
def circle_area(radius):
    return math.pi * radius ** 2

def circle_perimeter(radius):
    return 2 * math.pi * radius

# Triangle (Heron's Formula)
def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def triangle_perimeter(a, b, c):
    return a + b + c

# Main function
def main():
    while True:
        print("\nArea and Perimeter Calculator")
        print("-" * 30)
        print("1. Rectangle")
        print("2. Square")
        print("3. Circle")
        print("4. Triangle")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":  # Rectangle
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            print(f"Area: {rectangle_area(length, width)}")
            print(f"Perimeter: {rectangle_perimeter(length, width)}")

        elif choice == "2":  # Square
            side = float(input("Enter the side: "))
            print(f"Area: {square_area(side)}")
            print(f"Perimeter: {square_perimeter(side)}")

        elif choice == "3":  # Circle
            radius = float(input("Enter the radius: "))
            print(f"Area: {circle_area(radius)}")
            print(f"Perimeter (Circumference): {circle_perimeter(radius)}")

        elif choice == "4":  # Triangle
            a = float(input("Enter side A: "))
            b = float(input("Enter side B: "))
            c = float(input("Enter side C: "))
            print(f"Area: {triangle_area(a, b, c)}")
            print(f"Perimeter: {triangle_perimeter(a, b, c)}")

        elif choice == "5":  # Exit
            print("Exiting the calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
