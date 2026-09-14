#Write a program to prompt user to enter userid and password. If Id and
#password is incorrect give him chance to re-enter the credentials. Let him try 3
#times. After that program to terminate.

correct_id = 'safa'
correct_password = 1234

attempt = 1

while (attempt <= 3):

    user_id = input('Enter username: ')
    password = int(input('Enter password: '))

    if (user_id == correct_id and password == correct_password):
        print('Login successful')
        break

    else:
        print('Incorrect username or password')
        attempt = attempt + 1

if attempt > 3:
    print('You have used all 3 attempts. Program terminated.')