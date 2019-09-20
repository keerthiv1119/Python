'''
Author : Keerthi Vutukuri
Id : N151119
'''
Number_students = int(input("Enter the numeber of students").strip())
grades = []
for i in range(Number_students):
    marks = int(input("Enter each student marks").strip())
    grades.append(marks)
rounded_grades = []
for i in range(Number_students):
    r = grades[i] + ((5 - grades[i]) % 5) # Rounding to the next multiple of 5
    rounded_grades.append(r)
    difference = rounded_grades[i] - grades[i]
    if grades[i] >= 38:
        if difference < 3 and grades[i] < rounded_grades[i]:
            grades[i] = rounded_grades[i]
    else:
        grades[i] = grades[i]
for i in range(Number_students):
    print(grades[i])
