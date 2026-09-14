#Write a program to swap two numbers using third variable.

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

temp = a
a = b
b = temp

print(f'After swapping, first number is {a}')
print(f'After swapping, second number is {b}')