#Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

gender = input('Enter the gender(M/F): ')
age = int(input('Enter the age: '))

if(gender == 'F'):
    if(age >= 18):
        print('Girl is eligible for marraige.')

    else:
        print('Pehle Padhai karle!!')

else:
    if(age >= 21):
        print('Boy is eligible for marriage')

    else: 
        print('Kama le pehle!!')