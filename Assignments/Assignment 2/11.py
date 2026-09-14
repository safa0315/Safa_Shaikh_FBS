#Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

amount = int(input('Enter amount: '))

note200 = amount // 200
amount = amount % 200

note50 = amount // 50
amount = amount % 50

note20 = amount // 20
amount = amount % 20

note10 = amount // 10
amount = amount % 10

note5 = amount // 5
amount = amount % 5

note2 = amount // 2
amount = amount % 2

note1 = amount // 1
amount = amount % 1

total = note200 + note50 + note20 + note10 + note5 + note2 + note1

print(f'Minimum number of notes needed is {total}')