#Write a program to check if user has entered correct userid and password.

id = 'safa'
passw = 1234

user_id = input("Enter username: ")
password = int(input('Enter password: '))

if(user_id == id and password == passw):
    print('Entered correct id and password')

else: 
    print('Incorrect id and password')
