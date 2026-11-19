import random

print("--- DICE SIMULATOR ---")
total_rolls = 0
counts = {number: 0 for number in range(1, 7)}

while True:
    choice = input("\nPress Enter to roll the dice or type 'q' to quit: ")

    if choice.lower() == "q":
        break

    result = random.randint(1, 6)
    total_rolls += 1
    counts[result] += 1

    print(f"You rolled: {result}")

print("\n--- ROLL SUMMARY ---")
print(f"Total rolls: {total_rolls}")
for number, count in counts.items():
    print(f"Number {number}: {count} time(s)")

print("Thanks for playing!")
