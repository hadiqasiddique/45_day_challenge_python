def hex_to_rgb(hex_code):
    """
    Convert a hexadecimal color code to an RGB tuple.
    
    Args:
        hex_code (str): Hexadecimal color code (with or without '#').
    
    Returns:
        tuple: (R, G, B) values as integers.
    """
    # Remove '#' if present
    hex_code = hex_code.lstrip('#')

    # Validate length
    if len(hex_code) != 6:
        raise ValueError("Hex code should be exactly 6 characters long.")

    # Convert hex pairs to integers
    r = int(hex_code[0:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)

    return r, g, b


def main():
    print("Hex to RGB Conversion\n")

    while True:
        hex_code = input("Enter a hex code or type 'exit' to quit: ").strip()

        # Exit condition
        if hex_code.lower() == "exit":
            print("Program terminated.")
            break

        try:
            r, g, b = hex_to_rgb(hex_code)
            print(f"RGB Value: ({r}, {g}, {b})\n")
        except ValueError as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
