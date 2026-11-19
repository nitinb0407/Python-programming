# MODULE 2 - LAB EXERCISE 3
# Fibonacci Series Using Recursion

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


terms = int(input("Enter the number of terms: "))

if terms <= 0:
    print("Please enter a positive number of terms.")
else:
    print("Fibonacci series:")
    for i in range(terms):
        print(fibonacci(i), end=" ")
    print()


# SAMPLE INPUT
# Enter the number of terms: 7
#
# SAMPLE OUTPUT
# Fibonacci series:
# 0 1 1 2 3 5 8
