import random
import matplotlib.pyplot as plt

def roll_die(num_rolls):
    """Simulate rolling a die multiple times.
    Args:
        num_rolls (int): Number of times to roll the die.

    Returns:
        list: A list of integers representing the dice faces rolled."""
    return [random.randint(1, 6) for _ in range(num_rolls)]

def plot_histogram(results):
    """Plot a histogram of dice roll results.

    Args:
        results (list): List of integers representing dice roll results."""
    
    plt.hist(results, bins=range(1, 8), edgecolor='black', align='left')
    plt.title("Histogram of Dice Rolls")
    plt.xlabel("Dice Face")
    plt.ylabel("Frequency")
    plt.xticks(range(1, 7))
    plt.show()

def main():
    """Main function to run the Dice Roll Histogram program."""
    try:
        num_rolls = int(input("Enter the number of times to roll the die: "))
        if num_rolls <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    results = roll_die(num_rolls)
    plot_histogram(results)

if __name__ == "__main__":
    main()
