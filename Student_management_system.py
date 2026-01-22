# Student Management System

class Student:
    def __init__(self, name, matric_number):
        self.name = name
        self.matric_number = matric_number


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, matric_number):
        student = Student(name, matric_number)
        self.students.append(student)

    def display_students(self):
        print("Student Records:")
        for student in self.students:
            print("Name:", student.name, "| Matric Number:", student.matric_number)


# Program execution
sms = StudentManagementSystem()
sms.add_student("Azeez Atilola", "25/18022")
sms.display_students()
