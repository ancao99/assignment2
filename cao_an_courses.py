"""
Program Description: 
    This program is designed for managing course information. 
    It includes functions for adding, updating, and removing courses from a database. 
    The program interacts with a module named 'cao_an_dummy,' which likely contains initial data for courses and students.

Author: Cao An
"""
import cao_an_dummy
courses = cao_an_dummy.course
students = cao_an_dummy.student


#function to remove a course to the database
def remove_course():
    while True: 
        course_code =input("Please enter course code. Enter q or quit to return the remove menu:")
        if course_code == "q" or course_code == "quit":
            print()
            break
        remove = courses.pop(course_code,"not found")
        for student_infor in students.values():
            if course_code in student_infor["Course"]:
                student_infor["Course"].remove(course_code)
        if remove != "not found":
            print(f"Course with course code {course_code} is removed.")
            print()
            break
        else:
            print(f"The {course_code} is {remove}. Please enter again. ")
            print()        
 
#function to remove a course to the database
def remove_all_course():
    courses.clear()
    for student_info in students.values():
        student_info["Course"] = []
    print("All courses are removed\n")

#function to print out the course in the database
def print_course(course_number):
    if course_number in courses:
        print(f'The information of {course_number} is: ')
        print('\tCourse Name: {}\n\tInstructor: {}'.format(courses[course_number]['CourseName'],courses[course_number]['Instructor']))
        print('\tCourse Location: {}\n\tDescription: {}'.format(courses[course_number]['Location'],courses[course_number]['Description']))
        print('\tStudent in the course: {}'.format(courses[course_number]['student']))
        print()
    else:
        print("The course name does not valid.\n")
        print()

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
    #check if the course_code is aldready in the course table or not
    while True:
        course_code = input("Enter the course code (eg:ABC1234): ")
        if course_code in courses:
            print("The {course_code} is aldready in the table. Please enter again.")
        else:
            break
    #check if the course_name is aldready in the course table or not. each course_code has only one course_name
    while True:
        course_name = input("Enter the course name: ")
        course_exists = any(course_info["CourseName"] == course_name for course_info in courses.values())
        if course_exists:
            print("The {course_name} is aldready in the table. Please enter again.")
        else:
            break
    instructor = input("Enter instructor's name: ")
    location = input("Enter the location: ")
    description = input("Enter the course's description: ")
    student =[]
    #inset student id to the course and also update in the student tabl
    while True:
        id = input("Enter student's id. Enter 'done' when finished: ")
        if id.lower() == "done":
            break
        id =int(id)
        if id not in students:
            print(f"Error: Student with '{id}' not found in the student dictionary.")
        else:
            student.append(id)
            students[id]["Course"].append(course_code)
    courses[course_code]={
        "CourseName": course_name,
        "Instructor": instructor,
        "Location": location,
        "Description":description,
        "student":student
    }
    print("A course is added\n")

#update a course information 
def update_course():
        while True:
            course_code = input("Enter the course code that you want to update:")
            print()
            if course_code  in courses:
                print("Course update menu: ")
                print("1. Update course name (enter name or n or 1)")
                print("2. Update instructor (enter instructor or i or 2)")
                print("3. Update location (enter location or l or 3)")
                print("4. Update description (enter description or d or 4)")
                print("5. Update student (enter student or s or 5)")
                print("6. Return to the update menu (enter quit or q or 6)")
                option= input("Enter your option: ")
                print()
                if option == "name" or option == "n" or option == "1":
                    update_name(course_code )
                    break
                elif option == "instructor" or option == "i" or option == "2":
                    update_instructor(course_code )
                    break
                elif option == "location" or option == "l" or option == "3":
                    update_location(course_code )
                    break
                elif option == "description" or option == "d" or option == "4":
                    update_description(course_code )
                    break
                elif option == "student" or option == "s" or option == "5":
                    update_student(course_code )
                    break
                elif option == "quit" or option == "q" or option == "6":
                    break
                else:
                    print("The option entered is not valid. Try again")
            else:
                print(f"{course_code} is not valid. Enter another course code.")

#update course name
def update_name(code):
    name = input("Enter the name: ")
    courses[code]["CourseName"] = name
    print("Update course infor")
    print()

#update course instructor
def update_instructor(code):
    instructor = input("Enter the instructor: ")
    courses[code]["Instructor"] = instructor
    print("Update course infor")
    print()

#update course location
def update_location(code):
    location = input("Enter the location: ")
    courses[code]["Location"] = location
    print("Update course infor")
    print()

#update course description
def update_description(code):
    description = input("Enter the description: ")
    courses[code]["Description"] = description
    print("Update course infor")
    print()

#update course student
def update_student(code):
    print("Update student menu:")
    print("1. Delete a student (enter delete or d or 1)")
    print("2. Adding a student (enter add or a or 2)")
    option = input("Enter your option: ")
    while True:
        id = int(input("Enter the student id: (Enter q or quit to return the update menu)"))
        if option == "delete" or option == "d" or option == "1":
            if id in courses[code]["student"]:
                students[id]["Course"].remove(code)
                courses[code]["student"].remove(id)
                print("course infor is updated")
                print()
                break
            else:
                print("The course code is not in the list")
        elif option == "add" or option == "a" or option == "2":
            try:
                if id in courses[code]["student"]:
                    print("Cannot add because the course is already in the list.")
                else:
                    if id in students:
                        courses[code]["student"].append(id)
                        students[id]["Course"].append(code)
                        print(f"course with course_code {code} added to student with id is {id}")
                        print("course infor is updated")
                        print()
                        break
                    else:
                        print(f"The student id '{id}' does not exist.")
            except KeyError:
                print(f"KeyError: The student id '{id}' does not exist.")
            except Exception as e:
                print(f"An error occurred: {e}")
        elif option == "q" or option == "quit":
            break
        else:
            print("The option is not valid.")