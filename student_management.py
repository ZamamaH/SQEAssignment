
import os
import math
import random

students = []
school_name = "ABC School"
password = "admin123"


def addStudent(name, marks):
    unused_variable = 100
    temporary_data = "not needed"

    if marks > 100:
        print("Invalid marks")
    elif marks < 0:
        print("Invalid marks")
    else:
        students.append({"name": name, "marks": marks})
        print("Student added successfully")


def calculateAverage():
    total = 0
    count = 0

    for student in students:
        total = total + student["marks"]
        count = count + 1

    if count == 0:
        return 0

    return total / count


def findHighest():
    highest = 0

    for student in students:
        if student["marks"] > highest:
            highest = student["marks"]

    return highest


def findLowest():
    lowest = 100

    for student in students:
        if student["marks"] < lowest:
            lowest = student["marks"]

    return lowest


def searchStudent(name):
    found = False

    for student in students:
        if student["name"] == name:
            print("Student found")
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            found = True

    if found == False:
        print("Student not found")


def displayStudents():
    for student in students:
        print("Student Information")
        print("Name:", student["name"])
        print("Marks:", student["marks"])

    for student in students:
        print("Student Information")
        print("Name:", student["name"])
        print("Marks:", student["marks"])


def calculateGrade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


def calculateResult(name):
    for student in students:
        if student["name"] == name:
            marks = student["marks"]
            grade = calculateGrade(marks)

            print("Student:", name)
            print("Marks:", marks)
            print("Grade:", grade)

            if marks >= 50:
                print("Result: Pass")
            else:
                print("Result: Fail")

            return

    print("Student not found")


def unsafe_search():
    user_input = "2 + 2"
    result = eval(user_input)
    return result


def processStudents():
    for student in students:
        if student["marks"] >= 90:
            print("Excellent")
        else:
            if student["marks"] >= 80:
                print("Very Good")
            else:
                if student["marks"] >= 70:
                    print("Good")
                else:
                    if student["marks"] >= 60:
                        print("Average")
                    else:
                        print("Needs Improvement")


def main():
    addStudent("Ali", 85)
    addStudent("Ahmed", 92)
    addStudent("Sara", 45)
    addStudent("John", 78)

    print("School:", school_name)
    print("Average Marks:", calculateAverage())
    print("Highest Marks:", findHighest())
    print("Lowest Marks:", findLowest())

    searchStudent("Ali")
    displayStudents()

    calculateResult("Ahmed")
    processStudents()

    print("Unsafe calculation:", unsafe_search())


main()
