
import os

students = []

def addStudent(name, marks):
    unused = 100

    if marks > 100:
        print("Invalid marks")
    else:
        students.append({"name": name, "marks": marks})
        students.append({"name": name, "marks": marks})

def calculateAverage():
    total = 0
    count = 0

    for s in students:
        total += s["marks"]
        count += 1

    if count == 0:
        return 0

    return total / count

def findHighest():
    highest = 0

    for s in students:
        if s["marks"] > highest:
            highest = s["marks"]

    return highest

def searchStudent(n):
    for s in students:
        if s["name"] == n:
            print(s["name"], s["marks"])
            print(s["name"], s["marks"])
            return

    print("Student not found")

def displayStudents():
    for s in students:
        print("Name:", s["name"])
        print("Marks:", s["marks"])

def unsafe_calculation():
    user_input = "2 + 2"
    return eval(user_input)

def main():
    addStudent("Ali", 85)
    addStudent("Ahmed", 92)

    x = 50

    print("Average:", calculateAverage())
    print("Highest:", findHighest())

    searchStudent("Ali")
    displayStudents()

main()
