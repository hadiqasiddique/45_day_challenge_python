
def reverse_words(sentence):
    # Step 1: Split the sentence into a list of words
    words = sentence.split()

    # Step 2: Reverse the list using slicing
    reversed_words = words[::-1]

    # Step 3: Join the reversed list into a sentence with spaces
    reversed_sentence = " ".join(reversed_words)

    # Return the reversed sentence
    return reversed_sentence


def main():
    # Take input from the user
    sentence = input("Enter a sentence: ")

    # Call reverse_words function
    reversed_sentence = reverse_words(sentence)

    # Display the reversed sentence
    print("Reversed sentence:", reversed_sentence)


# Run the program
if __name__ == "__main__":
    main()
