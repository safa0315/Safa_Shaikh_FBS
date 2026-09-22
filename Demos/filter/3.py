#strong:

def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


def get_factorial(digit):
    return factorial(digit)


def check_strong(num):
    digits = list(map(int, str(num)))

    factorials = list(map(get_factorial, digits))

    return sum(factorials) == num


num = int(input("Enter a number: "))

print(check_strong(num))