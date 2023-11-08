
import cao_an_dummy
import datetime
students = cao_an_dummy.student
courses = cao_an_dummy.course

#function to print a student information in the database
def print_student(id):
    if id in students:
        print(f'The information of student with {id} is: ')
        print('Name: {}\nMajor: {}'.format(students[id]['Name'],students[id]['Major']))
        print('Course: {}\nDate of birth: {}'.format(students[id]['Course'],students[id]['Date_Of_Birth']))
        print('GPA: {}\n'.format(students[id]['GPA']))
    else:
        print("The id is not valid.\n")

#function to print all student information in the database:
def print_all_student():
    for id, info in students.items():
        print(f"Student ID: {id}")
        print(f"\tName: {info['Name']}")
        print(f"\tMajor: {info['Major']}")
        print(f"\tCourses: {', '.join(info['Course'])}")
        print(f"\tDate of birth: {info['Date_Of_Birth']}")
        print(f"\tGPA: {info['GPA']}")
    print("Print all student informtion.")
    print()

#function to remove all students in the database
def remove_all_student():
    students.clear()
    print("All students are removed\n")

#function to remove a student to the database
def remove_student():
    while True:
        user=input("Please enter student id. Enter q or quit to return the remove menu:")
        if user == "q" or user == "quit":
            print()
            break
        id = int(user)
        remove = students.pop(id,"not found")
        if remove != "not found":
            print(f"Student with id {id} is removed")
            break
        else:
            print(f"The {id} is {remove}. Please enter again. ")

#function to add student to the database
def add_student():
    course = []
    id = int(input("Enter the student ID: "))
    name = input("Enter student's name: ")
    major = input("Enter student's major: ")
    while True:
        course_name = input("Enter student's course. Enter done when finish: ")
        while course_name != "done":
            course.append(course_name)
            course_name = input("Another course's name. Enter done when finish: ")
        else:
            break
    date = input("Enter student's date of birth (YYYY/MM/DD): ")
    date = datetime.datetime.strptime(date,'%Y/%m/%d')
    date = date.strftime('%Y/%m/%d')
    GPA = float(input("Enter student's GPA: "))
    students[id]={
        "Name": name,
        "Major": major,
        "Course": course,
        "Date_Of_Birth": date,
        "GPA": GPA
    }
    print("A student is added\n")
    print()

#update a student information
def update_student():
    while True:
        id = int(input("Enter the id of student that you want to update: "))
        if id in students:
            print("Student update menu: ")
            print("1. Update name (enter name or n or 1)")
            print("2. Update major (enter major or m or 2)")
            print("3. Update course (enter course or c or 3)")
            print("4. Update date of birth (enter dob or d or 4)")
            print("5. Update GPA (enter gpa or g or 5)")
            print("6. Return to the update menu (enter quit or q or 6)")
            option= input("Enter your option: ")
            if option == "name" or option == "n" or option == "1":
                update_name(id)
            elif option == "major" or option == "m" or option == "2":
                update_major(id)
            elif option == "course" or option == "c" or option == "3":
                update_course(id)
            elif option == "date" or option == "d" or option == "4":
                update_dob(id)
            elif option == "gpa" or option == "g" or option == "5":
                update_gpa(id)
            elif option == "quit" or option == "q" or option == "6":
                break
            else:
                print("The option entered is not valid. Try again")
        else:
            print("{id} is not valid. Enter another id.")

#update student name
def update_name(id):
    name = input("Enter the name: ")
    students[id]["Name"] = name

#update student major
def update_major(id):
    major = input("Enter the major: ")
    students[id]["Major"] = major


#update course menu
def update_course(id):
    print("Update course menu:")
    print("1. Delete a course (enter delete or d or 1)")
    print("2. Adding a course (enter add or a or 2)")
    option = input("Enter your option: ")
    course_code = input("Enter the course code: ")
    if option == "remove" or option == "r" or option == "1":
        if course_code in students[id]["Course"]:
            students[id]["Course"].remove(course_code)
        else:
            print("The course code is not in the list")
    elif option == "add" or option == "a" or option == "2":
        if course_code in students[id]["Course"]:
            print("Cannot add because the course is aldready in the list.")
        else:
            students[id]["Course"].append(course_code)
    else:
        print("The option is not valid.")

#update student date of birth
def update_dob(id):
    new_dob = input("Enter the new date of birth (YYYY/MM/DD): ")
    new_date = datetime.datetime.strptime(new_date, '%Y/%m/%d')
    students[id]["Date_Of_Birth"] = new_date.strftime('%Y/%m/%d')

#update student gpa
def update_gpa(id):
    gpa = input("Enter the gpa: ")
    students[id]["GPA"] = gpa