# Creating a class named sru_student to store student information
class sru_student:
    
    # Constructor to initialize object attributes
    def __init__(self, name, roll_no, hostel_status):
        self.name = name            # Store student name
        self.roll_no = roll_no      # Store student roll number
        self.hostel_status = hostel_status  # Store hostel status (Yes/No)
        self.fee_paid = False       # Initial fee status is unpaid

    # Method to update fee payment status
    def fee_update(self, status):
        self.fee_paid = status      # Update fee status based on user given value

    # Method to return all student details in a formatted string
    def display_details(self):
        return f"Name: {self.name}, Roll No: {self.roll_no}, Hostel: {self.hostel_status}, Fee Paid: {self.fee_paid}"


# -------- USER INPUT PART --------
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
hostel_status = input("Hostel student? (Yes/No): ")

# Creating an object of the class
student = sru_student(name, roll_no, hostel_status)

# Updating fee status based on user input
fee_status = input("Has the student paid the fee? (True/False): ")
student.fee_update(fee_status == "True")

# Displaying student details
print(student.display_details())
