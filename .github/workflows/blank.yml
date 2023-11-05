student_data = []
list_of_lists = []
nb = int(input("Please enter the number of students: "))
for i in range(nb):
    students = {}
    students["ID"] = int(input("Enter the student ID: "))
    students["Name"] = input("Enter the student name: ")
    students["Age"] = int(input("Enter the student age: "))
    students["Major"] = input("Enter the student major: ")
    students["GPA"] = float(input("Enter the student GPA: "))
    student_data.append(students)
    list_of_lists.append([students])
print(student_data)

def get_student_by_id(student_data, student_id):
    for student in student_data:
        if student["ID"] == student_id:
            return student
    return None

def get_all_students(student_data):
    return student_data

def get_students_by_major(student_data, major):
    return [student for student in student_data if student["Major"] == major]

def add_student(student_data, name, age, major, gpa):
    new_student = {
        "ID": len(student_data) + 1,
        "Name": name,
        "Age": age,
        "Major": major,
        "GPA": gpa
    }
    student_data.append(new_student)

#def find_common_majors(student_data1, student_data2):
#    majors1 = {student["Major"] for student in student_data1}
#    majors2 = {student["Major"] for student in student_data2}
#    return majors1.intersection(majors2)

def delete_student_by_id(student_data, student_id):
    for student in student_data:
        if student["ID"] == student_id:
            student_data.remove(student)

def calculate_average_gpa(student_data):
    if not student_data:
        return 0
    total_gpa = sum(student["GPA"] for student in student_data)
    return total_gpa / len(student_data)

def get_top_performers(student_data, num_top):
    sorted_students = sorted(student_data, key=lambda student: student["GPA"], reverse=True)
    top_students = sorted_students[:num_top]
    top_performers = [student["Name"] for student in top_students]
    return top_performers

while True:
    print("1. Get Student by ID")
    print("2. Get All Students")
    print("3. Get Students by Major")
    print("4. Add Student")
    print("5. Find Common Majors")
    print("6. Delete Student")
    print("7. Calculate Average GPA")
    print("8. Get Top Performers")
    print("9. Exit")
    print("- - - - - - - - - - - - - - -")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = int(input("Enter the student ID: "))
        student = get_student_by_id(student_data, student_id)
        if student:
            print(student)
        else:
            print("Student not found.")

    elif choice == "2":
        all_students = get_all_students(student_data)
        for student in all_students:
            print(student)

    elif choice == "3":
        major = input("Enter the major: ")
        students_in_major = get_students_by_major(student_data, major)
        if students_in_major:
            for student in students_in_major:
                print(student)
        else:
            print("No students found in the specified major.")

    elif choice == "4":
        name = input("Enter the student name: ")
        age = int(input("Enter the student age: "))
        major = input("Enter the student major: ")
        gpa = float(input("Enter the student GPA: "))
        add_student(student_data, name, age, major, gpa)
        print("Student added successfully.")

    elif choice == "5": 
        common_majors = set(list_of_lists[0][0]["Major"])
        for student_list in list_of_lists[1:]:
            major = student_list[0]["Major"]
            common_majors = common_majors.intersection({major})

        if common_majors:
            print("Common Majors:", common_majors)
        else:
            print("No common majors found among students.")

    elif choice == "6":
        student_id = int(input("Enter the student ID to delete: "))
        delete_student_by_id(student_data, student_id)
        print("Student deleted successfully.")

    elif choice == "7":
        avg_gpa = calculate_average_gpa(student_data)
        print("Average GPA: {:.2f}".format(avg_gpa))

    elif choice == "8":
        num_top = int(input("Enter the number of top performers to retrieve: "))
        top_performers = get_top_performers(student_data, num_top)
        print("Top Performers:", top_performers)

    elif choice == "9":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please select a valid option (1-9).")
