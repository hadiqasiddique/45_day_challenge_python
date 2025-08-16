# Name Acronym Generator
def generate_acronym(full_name):
    """Generates an acronym from a full name.
    Args:
        full_name (str): The full name of a person.
       
    Returns:
        str: Acronym formed from the initials of the name."""
    # Split the full name into words
    words = full_name.split()
    
    # Extract the first letter of each word and convert to uppercase
    acronym = ''.join(word[0].upper() for word in words)
    
    return acronym


def main():
    print("=== Name Acronym Generator ===\n")
    
    while True:
        # Take user input
        full_name = input("Enter your full name or type 'exit' to quit: ").strip()
        
        # Check if user wants to exit
        if full_name.lower() == 'exit':
            print("Exiting the acronym generator.")
            break
        
        # Generate acronym
        acronym = generate_acronym(full_name)
        
        # Display result
        print(f"The acronym for '{full_name}' is: {acronym}\n")


if __name__ == "__main__":
    main()
