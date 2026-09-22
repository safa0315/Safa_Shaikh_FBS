# Write a program to check if given number is Armstrong or not using recursive
# function.

def armstrong(num, original):
    if num == 0:
        return 0

    digit = num % 10

    return digit ** 3 + armstrong(num // 10, original)


num = int(input("Enter a number: "))

result = armstrong(num, num)

if result == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")