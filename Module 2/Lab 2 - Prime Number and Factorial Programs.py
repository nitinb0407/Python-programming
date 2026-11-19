# Lab Exercise 2: Prime Number and Factorial Programs

def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


print("PRIME NUMBER CHECK")
num = int(input("Enter a number: "))

if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")

print("\nFACTORIAL CALCULATOR")
fact_num = int(input("Enter a non-negative number: "))

if fact_num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial of", fact_num, "is", factorial(fact_num))
