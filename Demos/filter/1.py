#prime

def check_divisor(x):
    return num % x == 0


def check_prime(num):
    divisors = list(filter(check_divisor, range(1, num + 1)))

    return len(divisors) == 2


num = int(input("Enter a number: "))

print(check_prime(num))
