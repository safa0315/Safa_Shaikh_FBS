#Assignment4: Write a program to enter P, T, R and calculate simple Interest.

#Step1: Take input for p,t,r

p = int(input('Enter principal: '))
t = int(input('Enter time: '))
r = int(input('Enter rate: '))

#Calculate using SI formula
simpl_i = p*t*r/100

print(f'Simple Interest is {simpl_i}')