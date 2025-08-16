class SpanishTranslator:
    def __init__(self):
        # Predefined English → Spanish dictionary
        self.dictionary = {
    "hello": "hola",
    "world": "mundo",
    "good": "bueno",
    "morning": "mañana",
    "night": "noche",
    "thank": "gracias",
    "you": "tú",
    "thankyou": "gracias",  # new entry
    "my": "mi",
    "name": "nombre",
    "is": "es",
    "please": "por favor",
    "yes": "sí",
    "no": "no"
}

    def translate(self, text):
        # Split input text into words
        words = text.split()

        # Translate each word (keep original if not found)
        translated_words = [
            self.dictionary.get(word.lower(), word)
            for word in words
        ]

        # Join back into a string
        return " ".join(translated_words)


def main():
    translator = SpanishTranslator()

    while True:
        print("\n=== Spanish Translator ===")
        print("1. Translate text")
        print("2. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            text = input("Enter text to translate: ")
            translated_text = translator.translate(text)
            print(f"Translated text: {translated_text}")

        elif choice == 2:
            print("Exiting the translator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
