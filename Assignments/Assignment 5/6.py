#Write a program to print first n prime numbers.

n = int(input('Enter how many prime numbers you want: '))

count_prime = 0
num = 2

while count_prime < n:

    i = 2
    count = 0

    while i < num:

        if num % i == 0:
            count = count + 1

        i = i + 1

    if count == 0:
        print(num)
        count_prime = count_prime + 1

    num = num + 1