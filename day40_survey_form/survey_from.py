class Survey:
    def __init__(self, questions):
        """Initializes the survey with a list of questions and an empty dictionary for responses."""
        self.questions = questions
        self.responses = {}

    def conduct_survey(self):
        """ Conducts the survey by prompting the user for each question and storing the responses."""
        print("\nStarting the survey...\n")
        for question in self.questions:
            response = input(f"{question} \n> ").strip()
            self.responses[question] = response
        print("\nSurvey completed!\n")

    def display_results(self):
        """Displays all collected survey responses."""
        if not self.responses:
            print("\nNo responses collected yet.\n")
            return
        
        print("\nSurvey Results:")
        for question in self.responses:
            print(f"{question}: {self.responses[question]}")
        print()


def main():
    questions = [
        "What is your name?",
        "How old are you?",
        "What is your favorite programming language?"
    ]

    survey = Survey(questions)

    while True:
        print("Survey Menu:")
        print("1. Conduct Survey")
        print("2. Display Results")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: ").strip())
        except ValueError:
            print("Invalid input. Please enter a number 1, 2, or 3.\n")
            continue

        if choice == 1:
            survey.conduct_survey()
        elif choice == 2:
            survey.display_results()
        elif choice == 3:
            print("Exiting the survey application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.\n")

if __name__ == "__main__":
    main()
