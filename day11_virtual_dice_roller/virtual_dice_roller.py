
## **virtual_dice_roller.py**

import random

def roll_dice():
    """
    Simulate rolling two dice and return their values.
    Returns:
        tuple: (die1, die2) - integers between 1 and 6
    """
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2

def display_result(die1, die2):
    """
    Display the values of the dice and their total.
    Args:
        die1 (int): Value of the first die
        die2 (int): Value of the second die
    """
    print(f"\nYou rolled a {die1} and a {die2}")
    print(f"Total: {die1 + die2}")

def main():
    """
    Main function to run the dice roller.
    Continues rolling until the user chooses to quit.
    """
    while True:
        print("\nVirtual Dice Roller")
        roll = input("Press Enter to roll the dice or Q to quit: ").strip().lower()

        if roll == "q":
            print("Exiting the Dice Roller...")
            break

        die1, die2 = roll_dice()
        display_result(die1, die2)

if __name__ == "__main__":
    main()
