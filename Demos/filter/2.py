#perfect:


def check_divisor(x):
    return num % x == 0


def check_perfect(num):
    divisors = list(filter(check_divisor, range(1, num)))

    return sum(divisors) == num


num = int(input("Enter a number: "))

print(check_perfect(num))