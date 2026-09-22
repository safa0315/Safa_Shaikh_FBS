#armstrong:

def check_digit(x):
    return True


def check_armstrong(num):
    digits = list(filter(check_digit, map(int, str(num))))

    power = len(digits)

    total = sum(digit ** power for digit in digits)

    return total == num


num = int(input("Enter a number: "))

print(check_armstrong(num))