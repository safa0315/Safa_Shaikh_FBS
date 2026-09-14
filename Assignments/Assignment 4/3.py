#WAP to print sum of series upto n.

n = int(input('Enter n: '))

i = 1
total = 0

while i <= n:
    total = total + i
    i = i + 1

print('Sum is', total)