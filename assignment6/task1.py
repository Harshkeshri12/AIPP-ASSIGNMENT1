# Student class definition using constructor and method
class Student:
    def __init__(self, name, roll_no, course):
        self.name = name
        self.roll_no = roll_no
        self.course = course

    def display_details(self):
        print(f"Student Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")
        print(f"Course: {self.course}")

# Creating an object of Student class
student1 = Student("Harsh Raj", 101, "BCA")
student1.display_details()
