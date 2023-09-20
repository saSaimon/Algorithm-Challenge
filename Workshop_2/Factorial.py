
def factorial(n):
    factorial = 1
    for i in range(n, 0, -1):
        print(i)
        factorial = factorial*i
    print(factorial)


factorial(5)