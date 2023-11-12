"""
Program Description: 
    This program manages student information using dictionaries as a database. 
    It includes functions for adding, removing, printing, and updating student data. 
    The program also interacts with a 'cao_an_dummy' module, which presumably contains initial student and course data.

Author: Cao An
"""
import cao_an_dummy
import datetime
students = cao_an_dummy.student
courses = cao_an_dummy.course

#function to remove a student to the database
def remove_student():
    while True:
        user=input("Please enter student id. Enter q or quit to return the remove menu: ")
        if user == "q" or user == "quit":
            print()
            break
        id = int(user)
        remove = students.pop(id,"not found")
        for course_infor in courses.values():
            if id in course_infor["student"]:
                course_infor["student"].remove(id)
        if remove != "not found":
            print(f"Student with id {id} is removed")
            print()
            break
        else:
            print(f"The {id} is {remove}. Please enter again. ")
            print()


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
    for course_info in courses.values():
        course_info["student"] = []
    print("All students are removed\n")

#function to add student to the database
def add_student():
    course = []
    while True:
        id = int(input("Enter the student ID: "))
        if id in students:
            print(f"The {id} is aldready in the dictionary. Please enter again.")
        else:
            break
    name = input("Enter student's name: ")
    major = input("Enter student's major: ")
    while True:
        course_name = input("Enter student's course. Enter 'done' when finished:(enter ABC1234 or ABCD1234) ")
        if course_name.lower() == "done":
            break
        elif course_name not in courses:
            print(f"Error: Course '{course_name}' not found in the course dictionary.")
        else:
            course.append(course_name)
            courses[course_name]["student"].append(id)
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
            print()
            if option == "name" or option == "n" or option == "1":
                update_name(id)
                break
            elif option == "major" or option == "m" or option == "2":
                update_major(id)
                break
            elif option == "course" or option == "c" or option == "3":
                update_course(id)
                break
            elif option == "date" or option == "d" or option == "4":
                update_dob(id)
                break
            elif option == "gpa" or option == "g" or option == "5":
                update_gpa(id)
                break
            elif option == "quit" or option == "q" or option == "6":
                print()
                break
            else:
                print("The option entered is not valid. Try again")
                print()
        else:
            print("{id} is not valid. Enter another id.")
        

#update student name
def update_name(id):
    name = input("Enter the name: ")
    students[id]["Name"] = name
    print("Student info is updated.")
    print()
    

#update student major
def update_major(id):
    major = input("Enter the major: ")
    students[id]["Major"] = major
    print("Student info is updated.")
    print()


#update course menu
def update_course(id):
    print()
    print("Update course menu:")
    print("1. Delete a course (enter delete or d or 1)")
    print("2. Adding a course (enter add or a or 2)")
    option = input("Enter your option: ")
    while True:
        course_code = input("Enter the course code: (Enter q or quit to return the update menu)")
        if option == "delete" or option == "d" or option == "1":
            if course_code in students[id]["Course"]:
                students[id]["Course"].remove(course_code)
                courses[course_code]["student"].remove(id)
                break
            else:
                print("The course code is not in the list")
        elif option == "add" or option == "a" or option == "2":
            try:
                if course_code in students[id]["Course"]:
                    print("Cannot add because the course is already in the list.")
                else:
                    if course_code in courses:
                        courses[course_code]["student"].append(id)
                        students[id]["Course"].append(course_code)
                        print(f"Student with ID {id} added to course {course_code}")
                        break
                    else:
                        print(f"The course code '{course_code}' does not exist.")
            except KeyError:
                print(f"KeyError: The course code '{course_code}' does not exist.")
            except Exception as e:
                print(f"An error occurred: {e}")
        elif option == "q" or option == "quit":
            break
        else:
            print("The option is not valid.")
    print("Student info is updated.")
    print()

#update student date of birth
def update_dob(id):
    date = input("Enter student's date of birth (YYYY/MM/DD): ")
    date = datetime.datetime.strptime(date,'%Y/%m/%d')
    date = date.strftime('%Y/%m/%d')
    students[id]["Date_Of_Birth"] = date
    print("Student info is updated.")
    print()

#update student gpa
def update_gpa(id):
    gpa = input("Enter the gpa: ")
    students[id]["GPA"] = gpa
    print("Student info is updated.")
    print()