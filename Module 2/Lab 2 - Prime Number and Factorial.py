# Lab Exercise 2: Prime Number and Factorial Programs

# Prime number check
number = int(input("Enter a number to check whether it is prime: "))

if number <= 1:
    print(number, "is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")

# Factorial calculation
n = int(input("\nEnter a number to find its factorial: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print("Factorial of", n, "is", factorial)
