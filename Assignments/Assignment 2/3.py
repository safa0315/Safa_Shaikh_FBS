#Convert distance given in feet and inches into meter and centimeter.
# 1 foot= 30.48 cm
#1 inch = 2.54 cm
#1 metre = 100 cm

dist_feet = int(input('Enter distance in feet: '))
dist_inch = int(input('Enter distance in inch: '))

metre_feet = dist_feet*0.3048
metre_inch = dist_inch*0.0254

total_m = metre_feet + metre_inch

total_cm = total_m*100


print(f'DIstance is {total_m} meters and {total_cm} centimeters')

