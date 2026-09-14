#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

a = int(input('Enter side 1: '))
b = int(input('Enter side 2: '))
c = int(input('Enter side 3: '))

if(a == b == c):
    print('Triangle is equilateral.')
    
elif(a ==b or b== c or a==c):
    print('Triangle is isosceles.')

else:
    print('Triangle is scalene.')



