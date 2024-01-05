from tkinter import *

'''
    Student management system.

    This is a menu based system that allows users to perform various features.
    The features include the following;

    1. Create student object
        [
            Attributes of a student
            - name
            - roll number
            - grade
            - marks
        ]
    2. Add new student instance
    3. Display student information based on roll number
    4. Calculate the grade of a student based on marks
    5. Update student information based on roll number
    6. Delete students based on roll number 
    
    By Okiror Samuel Vinald
'''


class Student:
    
    ''' ------ student class -------- '''

    def __init__(self, name, roll_number, grade, marks):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade
        self.marks = marks

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_roll_number(self):
        return self.roll_number

    def set_roll_number(self, roll_number):
        self.roll_number = roll_number

    def get_grade(self):
        return self.grade

    def set_grade(self, grade):
        self.grade = grade

    def get_marks(self):
        return self.marks

    def set_marks(self, marks):
        self.marks = marks

    def calculate_grade(self):
        if self.marks < 0 or self.marks > 100:
            return None
        elif self.marks >= 90:
            return 'A'
        elif self.marks >= 80:
            return 'B'
        elif self.marks >= 70:
            return 'C'
        elif self.marks >= 60:
            return 'D'
        elif self.marks >= 50:
            return 'P'
        else:
            return 'F'


#  ---------------- End of the student class ---------------- 


def add_student():
    
    """ -------- Add a new student -------- """
    
    name = name_entry.get()
    roll_number = roll_entry.get()
    marks_str = marks_entry.get()

    try:
        marks = float(marks_str)
    except ValueError:
        invalid_label.config(text="Invalid mark entry. Marks should be a number.")
        window.after(3000, clear_error_label)
        return

    new_student = Student(name, roll_number, "", marks)
    grade = new_student.calculate_grade()

    if grade is None:
        invalid_label.config(text="Invalid mark entry. Unable to calculate grade.")
        window.after(3000, clear_error_label)
        return

    new_student.set_grade(grade)
    students.append(new_student)

# ---------------- Clear input fields --------------------
    
    name_entry.delete(0, END)
    roll_entry.delete(0, END)
    marks_entry.delete(0, END)
    invalid_label.config(text="")


#  ---------------- End of the add new student ----------------


def display_student_info():
    """ -------- Display the information of a specific student -------- """

    roll_number = roll_entry.get()
    found = False

# ---------------- Clear error label ------------------------------

    invalid_label.config(text="")

    for student in students:
        if student.get_roll_number() == roll_number:
            info_label.config(
                text=f"Name: {student.get_name()}\nRoll Number: {student.get_roll_number()}\nGrade: {student.get_grade()}\nMarks: {student.get_marks()}"
            )
            window.after(7000, clear_info_label)
            found = True
            break

    if not found:
        info_label.config(text=f"Student with roll number {roll_number} not found.")
        window.after(3000, clear_info_label)

#  ---------------- End of the display student information ----------------


def delete_student():
    """ -------- Delete a student -------- """

    roll_number = roll_entry.get()
    found = False

    invalid_label.config(text="")

    for student in students:
        if student.get_roll_number() == roll_number:
            students.remove(student)
            info_label.config(text=f"Student with roll number {roll_number} deleted.")
            window.after(5000, clear_info_label)
            found = True
            break

    if not found:
        info_label.config(text=f"Student with roll number {roll_number} not found.")
        window.after(3000, clear_info_label)
        

#  ---------------- End of the delete student ----------------

def update_student_info():
    """ -------- Update the information of a specific student -------- """

    roll_number = roll_entry.get()
    found = False

    invalid_label.config(text="")

    for student in students:
        if student.get_roll_number() == roll_number:
            new_name = name_entry.get()
            if new_name:
                student.set_name(new_name)
            new_roll_number = roll_entry.get()
            if new_roll_number:
                student.set_roll_number(new_roll_number)
            new_marks_str = marks_entry.get()
            if new_marks_str:
                try:
                    new_marks = float(new_marks_str)
                except ValueError:
                    invalid_label.config(text="Invalid mark entry. Marks should be a number.")
                    window.after(3000, clear_error_label)
                    return
                student.set_marks(new_marks)
                student.set_grade(student.calculate_grade())
            info_label.config(text="Student information updated.")
            window.after(3000, clear_info_label)
            found = True
            break

    if not found:
        info_label.config(text=f"Student with roll number {roll_number} not found.")
        window.after(3000, clear_info_label)
        
#  ---------------- End of the update student information ----------------


def exit_program():
    """ -------- Exit the program -------- """
    window.destroy()


def clear_error_label():
    """ -------- Clear the error label.-------- """ 
    invalid_label.config(text="")


def clear_info_label():
    """ -------- Clear the error label.-------- """ 
    info_label.config(text="")


# ----------------- empty list of students -------------------
students = []


# ----------------- Create the main window -------------------
window = Tk()

window.title("Student Management System")
window.config(padx=50, pady=10)


# ----------------- Create labels and entry fields -------------------
roll_label = Label(window, text="Roll Number:")
roll_label.grid(row=0, column=0, padx=10, pady=5, sticky="E")

roll_entry = Entry(window)
roll_entry.grid(row=0, column=1, padx=10, pady=10)

name_label = Label(window, text="Name:")
name_label.grid(row=1, column=0, padx=10, pady=5, sticky="E")

name_entry = Entry(window)
name_entry.grid(row=1, column=1, padx=10, pady=10)

marks_label = Label(window, text="Marks:")
marks_label.grid(row=2, column=0, padx=10, pady=5, sticky="E")

marks_entry = Entry(window)
marks_entry.grid(row=2, column=1, padx=10, pady=10)


# ----------------- Create a frame for buttons -------------------
button_frame = Frame(window)
button_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


# ----------------- Create buttons -------------------
add_button = Button(button_frame, text="Add Student", command=add_student)
add_button.pack(pady=5)

display_button = Button(button_frame, text="Display Student", command=display_student_info)
display_button.pack(pady=5)

update_button = Button(button_frame, text="Update Student", command=update_student_info)
update_button.pack(pady=5)

delete_button = Button(button_frame, text="Delete Student", command=delete_student)
delete_button.pack(pady=5)

exit_button = Button(button_frame, text="Exit", command=exit_program)
exit_button.pack(pady=5)

# ----------------- Create a label to display student information -------------------
info_label = Label(window, text="")
info_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

invalid_label = Label(window, text="")
invalid_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# ----------------- Create a responsive window layout -------------------
window.grid_columnconfigure(1, weight=1)

window.mainloop()
