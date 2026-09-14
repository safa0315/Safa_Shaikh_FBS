#WAP to check if given number is Perfect Number.

n = int(input('Enter a number: '))

i = 1
total = 0

while i < n:
    if n % i == 0:
        total = total + i
    i = i + 1

if total == n:
    print('Perfect Number')
else:
    print('Not a Perfect Number')