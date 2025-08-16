from collections import Counter
import string

# Function to read the file
def read_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return []

# Function to count lines
def count_lines(file_content):
    return len(file_content)

# Function to count total words
def count_words(file_content):
    word_count = 0
    for line in file_content:
        words = line.split()
        word_count += len(words)
    return word_count

# Function to find most frequent words
def most_frequent_words(file_content, num_words=10):
    words = []
    for line in file_content:
        words.extend(line.translate(str.maketrans('', '', string.punctuation)).lower().split())
    word_counter = Counter(words)
    return word_counter.most_common(num_words)

# Function to display all statistics
def display_statistics(file_path):
    content = read_file(file_path)
    if content:
        print(f"Line Count: {count_lines(content)}")
        print(f"Word Count: {count_words(content)}")
        print("Most Frequent Words:")
        for word, count in most_frequent_words(content):
            print(f"{word}: {count}")

# Main function
def main():
    file_path = input("Enter the file path of the text file to be analyzed: ")
    display_statistics(file_path)

if __name__ == "__main__":
    main()
