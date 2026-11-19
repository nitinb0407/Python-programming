"""
MODULE 5 - LAB 3: DICE SIMULATOR USING RANDOM MODULE

Sample run:
===== DICE SIMULATOR =====
Press Enter to roll the dice or type q to quit: [Enter]
You rolled: 4
Press Enter to roll the dice or type q to quit: q
Total rolls: 1
Thanks for playing!
"""

import random

def roll_dice():
    return random.randint(1, 6)


def main():
    print("===== DICE SIMULATOR =====")
    total_rolls = 0
    counts = {number: 0 for number in range(1, 7)}

    while True:
        command = input("\nPress Enter to roll the dice or type q to quit: ")
        if command.lower() == "q":
            break
        if command != "":
            print("Press Enter to roll or q to quit.")
            continue

        result = roll_dice()
        total_rolls += 1
        counts[result] += 1
        print(f"You rolled: {result}")

    print(f"\nTotal rolls: {total_rolls}")
    if total_rolls:
        print("Roll statistics:")
        for number, count in counts.items():
            print(f"{number}: {count} time(s)")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
