#Write a program to reverse three-digit number.

num = int(input('Enter a three digit number: '))

digit1 = num // 100
digit2 = (num // 10) % 10
digit3 = num % 10

print(f' Reversed number is {digit3}{digit2}{digit1}')