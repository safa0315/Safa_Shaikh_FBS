#Assignment7: Program to Find the Roots of a Quadratic Equation

a = int(input('Enter value of a: ' ))
b = int(input('Enter value of b: ' ))
c = int(input('Enter value of c: ' ))


root_1 = (-b + (b**2 -4*a*c)**0.5)/(2*a)

root_2 = (-b - (b**2 -4*a*c)**0.5)/(2*a)

print(f'Root 1 is {root_1} and Root 2 is {root_2}')
