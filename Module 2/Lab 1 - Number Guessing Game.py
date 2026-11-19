# Lab Exercise 1: Number Guessing Game

import random

secret_number = random.randint(1, 100)
attempts = 0

print("NUMBER GUESSING GAME")
print("Guess a number between 1 and 100.")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
        elif guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number.")
            print("Number of attempts:", attempts)
            break
    except ValueError:
        print("Please enter a valid whole number.")
