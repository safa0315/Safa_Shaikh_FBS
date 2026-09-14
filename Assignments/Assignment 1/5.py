#Assignment5: Write a program to enter P, T, R and calculate Compound Interest.

#Step1: Take input for p,r,t

p = int(input('Enter principal: '))
t = int(input('Enter time: '))
r = int(input('Enter rate: '))

#Step2: Calculate CI
amount = p * (pow((1 + r/100), t)) #pow is a built in function used to calculate powers
#so pow(base, exponent) originally the formula for amount is p(1+r/100)^t here base is (1+r/100) while exponent is t
#hence pow
comp_int = amount - p

#Step3: Display CI
print("Compund Interest is", comp_int)