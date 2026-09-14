#Enter number of students from user. For those many students accept marks of 5
#subject marks from user and calculate percentage. Display all percentage and
#average percentage of students.

students = int(input('Enter number of students: '))

total_percentage = 0

student = 1

while student <= students:

    total_marks = 0
    subject = 1

    while subject <= 5:

        marks = int(input(f'Enter marks of subject {subject}: '))
        total_marks = total_marks + marks

        subject = subject + 1

    percentage = total_marks / 5

    print(f'Percentage of student {student} is {percentage}%')

    total_percentage = total_percentage + percentage

    student = student + 1

average = total_percentage / students

print(f'Average percentage is {average}%')