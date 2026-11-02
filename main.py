
students = []

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")
        age = input("Enter age: ")
        course = input("Enter course: ")

        student = {
            "Name": name,
            "Roll Number": roll_no,
            "Age": age,
            "Course": course
        }

        students.append(student)
        print("\nStudent details added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("\nNo student details found!")
        else:
            print("\n--- Student Details ---")

            for student in students:
                print("Name:", student["Name"])
                print("Roll Number:", student["Roll Number"])
                print("Age:", student["Age"])
                print("Course:", student["Course"])
                print("----------------------")

    elif choice == "3":
        print("Exiting Student Management System...")
        break

    else:
        print("Invalid choice! Try again.")
