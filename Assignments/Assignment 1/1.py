#Assignement1: Write a program to calculate the percentage of student based on marks of any 5 subjects.

#Step 1: Take the input of 5 subjects

num1 = int(input('Enter marks of Maths:' ))
num2 = int(input('Enter marks of English:' ))
num3 = int(input('Enter marks of Science:' ))
num4 = int(input('Enter marks of History:' ))
num5 = int(input('Enter marks of Geography:' ))

#Also take the input of total marks
total_marks = int(input('Enter Total marks:' ))

#Add all the marks of the subjects
sum = num1 + num2 + num3 + num4 + num5

#Calculate percentage
percent = sum*100/total_marks


#Display the percentage
print(f'Percentage is {percent}')

