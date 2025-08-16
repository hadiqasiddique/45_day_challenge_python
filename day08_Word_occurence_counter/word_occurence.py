import re
from collections import Counter

def count_word_occurrences(text):
    """
    Count how many times each word appears in a given text.
    This function is case-insensitive and ignores punctuation.
    Args:
        text (str): The input sentence or paragraph.
    Returns:
        dict: A dictionary with words as keys and their counts as values.
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation using regex (only keep letters and numbers)
    words = re.findall(r'\b\w+\b', text)
    
    # Count words using Counter
    word_counts = Counter(words)
    
    return word_counts


def main():
    # Step 1: Get input from user
    sentence = input("Enter a sentence to count the word occurrences: ")
    
    # Step 2: Count words
    word_counts = count_word_occurrences(sentence)
    
    # Step 3: Display results
    print("\nWord Occurrences:")
    print("-" * 30)
    for word, count in sorted(word_counts.items()):
        print(f"{word:<15} {count}")
    print("-" * 30)

if __name__ == "__main__":
    main()
