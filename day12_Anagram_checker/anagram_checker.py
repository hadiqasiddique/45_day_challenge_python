
#Anagram Checker

def sanitize_input(input_str):
    """Sanitize input by converting to lowercase and removing spaces."""
    return ''.join(input_str.lower().split())

def are_anagrams(str1, str2):
    """ Check if two strings are anagrams by comparing their sorted characters. """
    str1 = sanitize_input(str1)
    str2 = sanitize_input(str2)
    return sorted(str1) == sorted(str2)

def main():
    print("=== Anagram Checker ===")
    
    # Take user input
    str1 = input("Enter your first string: ")
    str2 = input("Enter your second string: ")
    
    # Check if anagrams and print result
    if are_anagrams(str1, str2):
        print(f"{str1} and {str2} are anagrams!")
    else:
        print(f"{str1} and {str2} are not anagrams.")

# Call main function
if __name__ == "__main__":
    main()
