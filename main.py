amount_of_students = int(input("How many students are in the class? "))

students = []

students_info = []

for i in range(amount_of_students):
    a = str(input("Enter the student's name: "))
    b = float(input("Enter the student's math grade: "))
    c = float(input("Enter the student's english grade: "))
    d = float(input("Enter the student's science grade: "))
    def avg(b, c, d):
        return (b + c + d) / 3
    total = b + c + d
    average = avg(b, c, d)
    students_stats = f"Name: {a}, Total: {total}, Average: {average}"
    students.append(average)
    students_info.append(students_stats)
    print (f"{a} - Average is {average} - Total is {total}")
    if average < 60:
        print("Failed")
    else:
        print("Passed")

number = int(input("Type the number based on what you want to see. 1 - Display All Students, 2 - Search for a Student, 3 - Show Top Student, 4 - Class Statistics, 5 - Failed Students, 6 - Sort Students, 7 - Exit"))

while number != 7:


    if number == 1:
        print(students_info)

    elif number == 2:
        search = input("Enter the students name:").lower()
        student_match = [item for item in students_info if search in item.lower()]
        print(student_match)

    elif number == 3:
        students.sort(reverse=True)
        print(students[0])
        student_score = input("Enter the average given and you will know who got that average:")
        student_match2 = [item for item in students_info if float(student_score) == (item[2])]
        print(student_match2)

    elif number == 4:
        class_average = sum(students) / len(students)
        print(f"The class average is {class_average:.2f}")
        count = 0
        students.sort(reverse=True)
        print(f"The highest average is {students[0]}")
        students.sort()
        print(f"The lowest average is {students[0]}")
        for average in students:
            if average < 60:
                count += 1
        print(f"The amount of students that failed are {count}.")
        count2 = 0
        for average in students:
            if average > 60:
                count2 += 1
        print(f"The amount of students that passed are {count2}.")


    elif number == 5:
        count = 0
        for average in students:
            if average < 60:
                count += 1
        print(f"The amount of students that failed are {count}.")
        if count == 0:
            print("Everyone passed!")

    elif number == 6:
        students.sort(reverse=True)
        print(students)

    number = int(input("Type the number based on what you want to see. 1 - Display All Students, 2 - Search for a Student, 3 - Show Top Student, 4 - Class Statistics, 5 - Failed Students, 6 - Sort Students, 7 - Exit"))

print("Thank you for using the Student Performance System!")
