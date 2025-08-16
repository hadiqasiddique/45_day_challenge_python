#voting system 
def display_menu():
    print("\n=====================")
    print("   Voting System")
    print("=====================")
    print("1. Vote")
    print("2. View Results")
    print("3. Exit")


def vote(options):
    print("\nVoting Options:")
    print("---------------")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    choice = input("\nEnter the number of your favorite option: ")

    # validate input
    if choice.isdigit() and 1 <= int(choice) <= len(options):
        return int(choice) - 1
    else:
        print("Invalid choice. Please try again.")
        return None


def display_results(votes, options):
    print("\nCounting votes...")
    print("Voting Results")
    print("--------------")
    for i, count in enumerate(votes):
        print(f"{options[i]} - {count} votes")


def main():
    # predefined options (customize as needed)
    options = ["Option 1", "Option 2", "Option 3"]
    votes = [0] * len(options)

    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            vote_choice = vote(options)
            if vote_choice is not None:
                votes[vote_choice] += 1
                print("Your vote has been recorded!")
        elif choice == 2:
            display_results(votes, options)
        elif choice == 3:
            print("👋 Exiting the voting system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
