# Lab Exercise 1: Number Guessing Game

import random

secret_number = random.randint(1, 50)
attempts = 0

print("NUMBER GUESSING GAME")
print("Guess a number between 1 and 50.")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < 1 or guess > 50:
            print("Please enter a number between 1 and 50.")
        elif guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Correct! You guessed the number in {attempts} attempts.")
            break
    except ValueError:
        print("Please enter a valid whole number.")
