"""
Program Description: 
This program is using the dictionary as a database.


Author: Cao An
"""
import cao_an_dummy
courses = cao_an_dummy.course
students = cao_an_dummy.student

#function to remove a course to the database
def remove_course():    
    while True:
        course_name=input("Please enter course code (eg:ABC1234). Enter q or quit to return the remove menu: ")
        remove = courses.pop(course_name,"not found")
        if course_name == "q" or course_name == "quit":
            print()
            break
        elif remove != "not found":
            print(f"course {course_name} is removed")
            break
        else:
            print(f"The {course_name} is {remove}. Please enter again. ")

#function to remove a course to the database
def remove_all_course():
    courses.clear()    
    print("remove all courses")

#function to print out the course in the database
def print_course(course_number):
    if course_number in courses:
        print(f'The information of {course_number} is: ')
        print('\tCourse Name: {}\n\tInstructor: {}'.format(courses[course_number]['CourseName'],courses[course_number]['Instructor']))
        print('\tCourse Location: {}\n\tDescription: {}'.format(courses[course_number]['Location'],courses[course_number]['Description']))
        print('\tStudent in the course: {}'.format(courses[course_number]['student']))
    else:
        print("The course name does not valid.\n")

#function to print out all the course in the database
def print_all_course():
    for name, info in courses.items():
        print(f"Course code: {name}")
        print(f"\tName: {info['CourseName']}")
        print(f"\tInstructor: {info['Instructor']}")
        print(f"\tCourses Location: {info['Location']}")
        print(f"\tDescription: {info['Description']}")
        print(f"\tStudent in the course: {info['student']}")
    print("Print all course information.")
    print()

#function to add a course to the database
def add_course():
    course_code = input("Enter the course code (eg:ABC1234): ")
    course_name = input("Enter the course name: ")
    instructor = input("Enter instructor's name: ")
    location = input("Enter the location: ")
    description = input("Enter the course's description: ")
    student =[]
    while True:
        student_id = int(input("Enter student's id. Enter done when finish: "))
        while student_id != "done":
            student.append(student_id)
            student_id = input("Another course's name. Enter done when finish: ")
        else:
            break
    courses[course_code]={
        "CourseName": course_name,
        "Instructor": instructor,
        "Location": location,
        "Description":description,
        "student":student
    }
    print("A course is added\n")
    print()

#update a course information 
def update_couse():
        while True:
            course_code = int(input("Enter the course code that you want to update: "))
            if course_code  in students:
                print("Course update menu: ")
                print("1. Update course name (enter name or n or 1)")
                print("2. Update instructor (enter instructor or i or 2)")
                print("3. Update location (enter location or l or 3)")
                print("4. Update description (enter description or d or 4)")
                print("5. Update student (enter student or s or 5)")
                print("6. Return to the update menu (enter quit or q or 6)")
                option= input("Enter your option: ")
                if option == "name" or option == "n" or option == "1":
                    update_name(course_code )
                elif option == "instructor" or option == "i" or option == "2":
                    update_instructor(course_code )
                elif option == "location" or option == "l" or option == "3":
                    update_location(course_code )
                elif option == "description" or option == "d" or option == "4":
                    update_description(course_code )
                elif option == "student" or option == "s" or option == "5":
                    update_student(course_code )
                elif option == "quit" or option == "q" or option == "6":
                    break
                else:
                    print("The option entered is not valid. Try again")
            else:
                print("{course_code} is not valid. Enter another course code.")

#update course name
def update_name(code):
    name = input("Enter the name: ")
    courses[code]["CourseName"] = name

#update course instructor
def update_instructor(code):
    try: 
        instructor = input("Enter the instructor: ")
        courses[code]["Instructor"] = instructor
    except Exception as e:
        print(e)

#update course location
def update_location(code):
    location = input("Enter the location: ")
    students[id]["Major"] = location

#update course description
def update_description(code):
    pass

#update course student
def update_student(code):
    pass