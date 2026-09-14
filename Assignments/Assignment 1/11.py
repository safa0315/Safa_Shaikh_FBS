#Assignment11: Find the area and circumference of circle.

#Step1: Take input for radius of circle

r = int(input('Enter radius of circle: '))

#Step2: Calculate area
area = 3.14*r**2

#Step3: Calculate circumference

circum = 2*3.14*r

print(f'Area is {area} and Circumference of circle is {circum}')