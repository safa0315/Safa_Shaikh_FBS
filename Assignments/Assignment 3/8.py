#Write a program to prompt user to enter userid and password. After verifying
#userid and password display a 4 digit random number and ask user to enter the
#same. If user enters the same number then show him success message otherwise
#failed. (Something like captcha)

id = 'safa'
passw = 1234

user_id = input("Enter username: ")
password = int(input('Enter password: '))

if(user_id == id and password == passw):
    print('Entered correct id and password')
    captcha = 4534
    captcha1 = int(input('Enter Captcha: '))
    if(captcha == captcha1):
        print('Success.')

    else: 
        print('Failed.')

else: 
    print('Incorrect id and password')
