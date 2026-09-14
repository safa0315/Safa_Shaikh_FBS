#Assignment6: Write a Program to input two angles from user and find third angle of the triangle.
#Step1: take input for angles
ang1 = int(input('Enter marks of angle 1: ' ))
ang2 = int(input('Enter marks of angle 2: ' ))

#Calculate third angle

ang3 = 180 - (ang1 + ang2)

#Display third angle
print("Third angle of triangle is", ang3)