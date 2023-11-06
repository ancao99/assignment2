import cao_an_dummy
courses = cao_an_dummy.courses

#function to add a course to the database
def add_course():
    return print("add a course")



#function to remove a course to the database
def remove_course():    
    return print("remove a course")



#function to remove a course to the database
def remove_all_course():
    courses.clear()    
    print("remove all courses")



#function to print out all the course in the database
def print_course(course_name):
    if id in courses:
        print(f'The information of {course_name} is: ')
        print('Course Name: {}\nInstructor: {}'.format(courses[course_name]['CourseName'],courses[id]['Instructor']))
        print('Course : {}\n'.format(students[id]['Course']))
    else:
        print("The id is not valid.\n")
"""
"CSC1301": {
        "CourseName": "Introduction to Computer Science",
        "Instructor": "Smith",
        "Location": "Room 101",
    },"""


#update a course information 
def update_couse():
    return print("update a course")