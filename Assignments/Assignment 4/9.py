#WAP to print all numbers in a range divisible by a given number.

start = int(input('Enter starting number: '))
end = int(input('Enter ending number: '))
num = int(input('Enter number: '))

i = start

while i <= end:
    if i % num == 0:
        print(i)
    i = i + 1