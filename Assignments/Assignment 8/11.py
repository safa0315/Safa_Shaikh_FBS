# 11. WAP to check if a given number is Armstrong number or not. For
# each task create separate functions.

def check_armstrong(num):
    original = num
    total = 0

    while num > 0:
        digit = num % 10
        total = total + digit ** 3
        num = num // 10

    if total == original:
        return True
    else:
        return False


num = int(input("Enter a number: "))

if check_armstrong(num):
    print("Armstrong number")
else:
    print("Not an Armstrong number")