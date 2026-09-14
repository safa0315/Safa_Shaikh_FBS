#Write a program to input angles of a triangle and check whether triangle is valid or not.
#total sum of angles in a tri= 180
ang1 = int(input('Enter angle 1: '))
ang2 = int(input('Enter angle 2: '))
ang3 = int(input('Enter angle 3: '))

if(ang1 + ang2 + ang3 == 180):
    print('The triangle is valid.')

else:
    print('Traingle is not valid.')