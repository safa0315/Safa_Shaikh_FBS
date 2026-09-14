#Write a program to input electricity unit charges and calculate total electricity bill
#according to the given condition:
#For first 50 units Rs. 0.50/unit
#For next 100 units Rs. 0.75/unit
#For next 100 units Rs. 1.20/unit
#For unit above 250 Rs. 1.50/unit
#An additional surcharge of 20% is added to the bill

unit = int(input('Total unit'))

if( 50>= unit ):
    price = unit*0.50
    print(f'Total bill is {price}')

elif(100 >= unit> 50):
    price = unit*0.75
    print(f'Total bill is {price}')

elif(250 >= unit> 100 ):
    price = unit*1.20
    print(f'Total bill is {price}')

else:
    price = unit*1.50
    print(f'Total bill is {price}')

