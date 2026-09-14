#Write a program to swap two numbers without using third variable.

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

a = a + b
b = a - b
a = a - b

print(f'After swapping, first number is {a}')
print(f'After swapping, second number is {b}')