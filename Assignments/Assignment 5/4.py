#WAP to print Armstrong number within a given range

start = int(input('Enter starting number: '))
end = int(input('Enter ending number: '))

num = start

while num <= end:

    original = num

    digits = 0
    temp = num

    while temp > 0:
        digits = digits + 1
        temp = temp // 10

    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total = total + digit ** digits
        temp = temp // 10

    if total == original:
        print(num)

    num = num + 1