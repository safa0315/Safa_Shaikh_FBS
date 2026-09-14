#Input 5 subject marks from user and display grade(eg.First class,Second class ..)

mark1 = int(input('Enter marks of subject 1: '))
mark2 = int(input('Enter marks of subject 2: '))
mark3 = int(input('Enter marks of subject 3: '))
mark4 = int(input('Enter marks of subject 4: '))
mark5 = int(input('Enter marks of subject 5: '))

total = mark1 + mark2 + mark3 + mark4 + mark5 
percent = (total*100)/500
if(percent >= 85):
    print('First Class.')

elif(85 > percent >= 65):
    print('Second Class')

elif(65> percent >= 35):
    print('Third Class.')

else:
    print('Fail.')