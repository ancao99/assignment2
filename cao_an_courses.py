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
        print('Course Name: {}\nInstructor: {}'.format(courses[course_number]['CourseName'],courses[course_number]['Instructor']))
        print('Course Location: {}\n'.format(courses[course_number]['Location']))
    else:
        print("The course name does not valid.\n")

#function to print out all the course in the database
def print_all_course():
    for name, info in courses.items():
        print(f"Course code: {name}")
        print(f"\tName: {info['CourseName']}")
        print(f"\tInstructor: {info['Instructor']}")
        print(f"\tCourses Location: {info['Location']}")
    print("Print all course information.")
    print()

#function to add a course to the database
def add_course():
    course_code = input("Enter the course code (eg:ABC1234): ")
    course_name = input("Enter the course name: ")
    instructor = input("Enter instructor's name: ")
    location = input("Enter the location's major: ")
    courses[course_code]={
        "CourseName": course_name,
        "Instructor": instructor,
        "Location": location,
    }
    print("A course is added\n")
    print()

#update a course information 
def update_couse():
    pass