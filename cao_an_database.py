"""
Program Description: 
This program is using the dictionary as a database.
Where to 

Author: Cao An
"""
import cao_an_students
import cao_an_courses

#print menu:
def print_menu():
    while True:
        print("1. Print a student's information (enter print student or ps or 1)")
        print("2. Print a course's information (enter print course or pc or 2)")
        print("3. Print all students (enter print all student or pas or 3)")
        print("4. Print all courses (enter print all course or pac or 4)")
        print("5. Enter q or quit or 5 to comeback to the main menu")
        user_input = input("Enter your choice:")
        if user_input == "1" or user_input.lower() == "ps" or user_input.lower() == "print student":
            id = int(input("Enter student's id: "))
            print()
            cao_an_students.print_student(id)
            break
        elif user_input == "2" or user_input.lower() == "pc" :
            cao_an_courses.print_course()
        elif user_input == "3" or user_input.lower() == "q" or user_input.lower() == "quit":
            print("Return to the main menu")
            break
        else:
            print("This is invalid. Please enter again")


while True:
    print("Menu:")
    print("1. Add a student or a course (enter add or a or 1)")
    print("2. Remove student or course (enter remove or r or 2)")
    print("3. Print all student or all the course or a student (enter print or p or 3)")
    print("4. Update the information (enter update or u or 4)")
    print("5. Enter quit or 5 to quit")
    user_input=input("Enter your option: ")
    print()
    if user_input == "1" or user_input.lower() == "add" or user_input.lower() == "a":
        #choose to add a student or a course
        while True:
            print("1. Add a student (enter as or 1)")
            print("2. Add a course (enter ac or 2)")
            print("3. Enter q or quit or 3 to comeback to the main menu")
            user_input=input("Enter your choice:")
            if user_input == "1" or user_input.lower() == "as":
                cao_an_students.add_student()
            elif user_input == "2" or user_input.lower() == "ac":
                cao_an_courses.add_course()
            elif user_input == "3" or user_input.lower() == "q" or user_input.lower() == "quit":
                print("Return to the main menu")
                break
            else:
                print("This is invalid. Please enter again")
    elif user_input.lower() == "remove" or user_input.lower() == "r" or user_input == "2":
        while True:
            print("1. Remove a student (enter rs or 1)")
            print("2. Remove a course (enter rc or 2)")
            print("3. Remove all students (enter ras or 2)")
            print("4. Remove all courses (enter rac or 2)")
            print("5. Enter q or quit or 5 to comeback to the main menu")
            user_input=input("Enter your choice:")
            if user_input == "1" or user_input.lower() == "rs":
                cao_an_students.remove_student()
            elif user_input == "2" or user_input.lower() == "rc":
                cao_an_courses.remove_course()
            elif user_input == "3" or user_input.lower() == "ras":
                cao_an_students.remove_all_student()
            elif user_input == "4" or user_input.lower() == "rac":
                cao_an_courses.remove_all_course()
            elif user_input == "5" or user_input.lower() == "q" or user_input.lower() == "quit":
                print("Return to the main menu")
                break
            else:
                print("This is invalid. Please enter again")
    elif user_input == "3" or user_input.lower() == "print" or user_input.lower() == "p":
        print_menu()
    elif user_input == "4" or user_input.lower() == "update" or user_input.lower() == "u":
        while True:
            print("1. Update a student (enter us or 1)")
            print("2. Update a course (enter uc or 2)")
            print("3. Enter q or quit or 3 to comeback to the main menu")
            user_input=input("Enter your choice:")
            if user_input == "1" or user_input.lower() == "us":
                cao_an_students.update_student()
            elif user_input == "2" or user_input.lower() == "uc":
                cao_an_courses.update_couse()
            elif user_input == "3" or user_input.lower() == "q" or user_input.lower() == "quit":
                print("Return to the main menu")
                break
            else:
                print("This is invalid. Please enter again")
    elif user_input == "5" or user_input == "quit" or user_input == "q":
        print("Thank you!! See you again soon.")
        break