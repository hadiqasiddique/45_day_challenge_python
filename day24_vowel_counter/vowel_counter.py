# Vowel Counter Project
# Function to count vowels in a string
def count_vowels(input_string):
    vowels = "aeiouAEIOU"  # All vowels in both lowercase and uppercase
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

# Main function
def main():
    print("===== Vowel Counter =====")
    input_string = input("Enter a string: ")
    total_vowels = count_vowels(input_string)
    print(f"The number of vowels in the string is: {total_vowels}")

# Run the program
if __name__ == "__main__":
    main()
