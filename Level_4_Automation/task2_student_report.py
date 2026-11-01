students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of student", i + 1)

    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))

    student = {
        "Name": name,
        "Marks": marks
    }

    students.append(student)

print("\n===== STUDENT REPORT =====")

for student in students:
    print("Name:", student["Name"])
    print("Marks:", student["Marks"])

    if student["Marks"] >= 90:
        grade = "A"
    elif student["Marks"] >= 75:
        grade = "B"
    elif student["Marks"] >= 60:
        grade = "C"
    elif student["Marks"] >= 40:
        grade = "D"
    else:
        grade = "Fail"

    print("Grade:", grade)
    print("----------------------")