# MODULE 2 - LAB EXERCISE 2
# Prime Number Check and Factorial Program

number = int(input("Enter a positive integer: "))

# Prime number check
if number < 2:
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
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print("Factorial of", number, "is", factorial)


# SAMPLE INPUT
# Enter a positive integer: 5
#
# SAMPLE OUTPUT
# 5 is a prime number.
# Factorial of 5 is 120
