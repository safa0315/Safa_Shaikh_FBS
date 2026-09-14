#2. Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)

#celc = int(input('Enter the temperature in Celcius: ')) should use float instead of int because temp may contain decimals
celc = float(input('Enter the temperature in Celcius: '))

far = ((celc / 5)*9) + 32
print(far)