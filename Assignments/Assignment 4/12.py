#Write a program to check if given number is Armstrong number or not.

num = int(input('Enter a number: '))

temp = num
count = 0
while(temp > 0):
    count += 1
    temp = temp // 10
# print(count)
    
temp = num
sum = 0
while(temp > 0):
    d = temp%10
    temp = temp // 10
    sum = sum +(d **count)
if(sum == num):
    print(f'{num} is an armstrong number.')
else:
    print(f'{num} is not an armstrong number.')    