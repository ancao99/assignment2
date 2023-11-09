"""
Program Description: 
This program is using to store the data-dummy values 

Author: Cao An
"""


student = {
    1: {
        "Name": "student1",
        "Major": "Computer Science",
        "Course": ["CSC1301",  "MATH2641"],
        "Date_Of_Birth" : "1999/01/15",
        "GPA": 4.0
    },
    2: {
        "Name": "student2",
        "Major": "Math",
        "Course": ["MATH2641", "MATH2215"],
        "Date_Of_Birth" : "2000/01/15",
        "GPA": 3.5
    },
    4: {
        "Name": "student4",
        "Major": "Computer Science",
        "Course": ["CSC1301", "CSC2720"],
        "Date_Of_Birth" : "2000/01/15",
        "GPA": 3.5
    },
    5: {
        "Name": "student5",
        "Major": "Data Science",
        "Course": ["CSC1301", "MATH2641"],
        "Date_Of_Birth" : "2000/01/15",
        "GPA": 3.5
    }

}

course = {
    "CSC1301": {
        "CourseName": "Introduction to Computer Science",
        "Instructor": "Instructor1",
        "Location": "Room 101",
        "Description":"This course is an introduction to the fundamental principles of programming and data analysis in computer science.",
        "student": [1,5,4]
    },

    "CSC2720": {
        "CourseName": "Data Structure",
        "Instructor": "Instructor2",
        "Location": "Room 101",
        "Description": "Basic concepts and analysis of data representation and associated algorithms.",
        "student":[4]

    },

    "MATH2641": {
        "CourseName": "Linear Algebra !",
        "Instructor": "Instructor3",
        "Location": "Room 201",
        "Description":"Theory and applications of matrix algebra, vector spaces, and linear transformations.",
        "student":[2,5,1]
    },

    "MATH2215": {
        "CourseName": "CALCULUS OF ONE VARIABLE II",
        "Instructor": "Instructor4",
        "Location": "Room 301",
        "Description":"Applications and techniques of integration; transcendental and inverse trigonometric functions; polar coordinates;"
                        "infinite sequences and series; indeterminate forms; improper integrals.",
        "student":[2]

    }
    
}