#Write a program to input all sides of a triangle and check whether triangle is valid or not.
#condition for sides:
#  a+b >c same for all sides

a = int(input('Enter side length: '))
b = int(input('Enter side length: '))
c = int(input('Enter side length: '))

if (a + b > c)and (a + c > b  ) and ( b + c > a):
    print('Triangle is valid')


else:
    print('Traingle is not valid')