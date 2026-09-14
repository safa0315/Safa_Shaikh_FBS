#Write a program to check if the given number is positive or negative.

num = int(input("Enter number: "))
if(num == 0):
    print('Number is neutral.')
elif(num > 0):
    print('Number is positive')
else:
    print('Number is negative.')