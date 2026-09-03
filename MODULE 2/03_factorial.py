# MODULE 2 - Lab Exercise 2
# Factorial Program

number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i

    print(f"Factorial of {number} = {factorial}")
