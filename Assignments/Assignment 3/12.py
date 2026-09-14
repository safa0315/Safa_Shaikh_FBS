#Write a program to check if given 3 digit number is a palindrome or not.

num = int(input('Enter Number: '))

dig1 = num // 100
dig2 = (num // 10) % 10
dig3 = num % 10

if(dig1 == dig3):
    print('Palindrome.')

else:
    print('Not palindrome.')