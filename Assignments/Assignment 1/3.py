#Assignemnt3: Program to find quotient and remainder of two numbers.

#Step1: Take input for dividend and divisor
num1 = int(input('Enter dividend 1:'))
num2 = int(input('Enter divisor 2:'))

#use modulus operator for finding remainder
remainder = num1%num2

#use floor division to find quotient #finds nearest integer if 3.5 then says 3
quotient = num1//num2

#Display remainder and quotient
print(f'Remainder of {num1} and {num2} is {remainder}')
print(f'Quotient of {num1} and {num2} is {quotient}')

