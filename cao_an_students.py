
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
    return print("update a student")