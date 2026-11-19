# MODULE 2 - LAB EXERCISE 1
# Number Guessing Game

import random

secret_number = random.randint(1, 20)
attempts = 0

print("I have selected a number between 1 and 20.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Correct! You guessed the number.")
        print("Number of attempts:", attempts)
        break


# SAMPLE OUTPUT (one possible run)
# I have selected a number between 1 and 20.
# Enter your guess: 8
# Too low! Try again.
# Enter your guess: 15
# Too high! Try again.
# Enter your guess: 12
# Correct! You guessed the number.
# Number of attempts: 3
#
# Note: The secret number is random, so output varies each run.
