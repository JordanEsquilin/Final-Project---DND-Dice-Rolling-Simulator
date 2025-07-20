import random
import csv
from datetime import datetime

# Dice class
class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self, times=1, modifier=0):
        rolls = [random.randint(1, self.sides) for _ in range(times)]
        total = sum(rolls) + modifier
        return {
            "individual": rolls,
            "modifier": modifier,
            "total": total
        }

# Log roll to CSV
def log_roll(dice_type, times, modifier, result):
    with open("rolls.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            dice_type,
            times,
            modifier,
            result["individual"],
            result["total"]
        ])

# Main function
def main():
    print("Welcome to the D&D Dice Rolling Simulator")

    dice_map = {
        "d4": Dice(4),
        "d6": Dice(6),
        "d8": Dice(8),
        "d10": Dice(10),
        "d12": Dice(12),
        "d20": Dice(20),
        "d100": Dice(100)
    }

    while True:
        print("\nAvailable Dice: d4, d6, d8, d10, d12, d20, d100")
        dice_type = input("Enter dice type (or 'quit' to exit): ").lower()
        if dice_type == 'quit':
            break

        if dice_type not in dice_map:
            print("Invalid dice type. Try again.")
            continue

        try:
            times = int(input("How many times to roll? "))
            modifier = int(input("Enter modifier (e.g. +2 or -1): "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        result = dice_map[dice_type].roll(times, modifier)
        print(f"\n Rolls: {result['individual']}")
        print(f" Modifier: {result['modifier']}")
        print(f" Total: {result['total']}")

        log_roll(dice_type, times, modifier, result)

    print("Thanks for playing. Good luck on your next adventure!")

if __name__ == "__main__":
    main()
