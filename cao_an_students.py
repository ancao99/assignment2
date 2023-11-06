
students = {
    1: {
        "Name": "An Cao",
        "Major": "Computer Science",
        "Course": ["CSC1301",  "CSC2720"],
        "Age": 24,
        "GPA": 4.0
    },
    2: {
        "Name": "Joe Doe",
        "Major": "Math",
        "Course": ["MATH2641", "MATH2215"],
        "Age": 18,
        "GPA": 3.5
    }
}

#update a student information
def update_student():
    return print("update a student")

#function to print out the a student information in the database
def print_student(id):
    if id in students:
        print(f'The information of student with id - {id} is: ')
        print('Student name: {}\nStudent major: {}'.format(students[id]['Name'],students[id]['Major']))
        print('Student course: {}\nStudent age: {}'.format(students[id]['Course'],students[id]['Age']))
        print('Student GPA: {}\n'.format(students[id]['GPA']))
    else:
        print("The id is not valid.\n")


#function to remove a course to the database
def remove_all_student():
    students.clear()
    print("All students are removed\n")

#function to remove a student to the database
def remove_student():
    while True:
        id=int(input("Please enter student id: "))
        remove = students.pop(id,"Not found")
        if remove != "Not found":
            break
    print(f"Student with id {id} is removed")

#function to add student to the database
def add_student():
    course = []
    id = int(input("Enter the student ID: "))
    name = input("Enter student's name: ")
    major = input("Enter student's major: ")
    while True:
        course = input("Enter student's address: (enter done when finish)")
        if course == "done":
            break
    age = int(input("Enter student's age: "))
    GPA = float(input("Enter student's GPA: "))
    students[id]={
        "Name": name,
        "Major": major,
        "Course": course,
        "Age": age,
        "GPA": GPA
    }
    print("A student is added")