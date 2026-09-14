#Assignment8: Write a program to convert days into years, weeks and days.


#Step1: Take input for days

days = int(input('Enter number of days: '))

#Step2: Calculate

weeks = days/7
years = weeks/12


#Step3: Display
print(f'{days} days are {weeks} weeks and {years} years')