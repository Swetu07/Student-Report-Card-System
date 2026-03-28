import json   # to save/load data 
import os    # to check if file exists

students = [] # each item will be a dict  →  { name, roll_number, marks }
DATA_FILE = "students_data.json"

#  FUNCTION 1 – Loading data from file on startup
#  (so data is not lost when I close the program)
def load_data():
    global students                         # I want to change the list above
    if os.path.exists(DATA_FILE):           # if the save-file already exists
        with open(DATA_FILE, "r") as f:
            students = json.load(f)         # fill students list from file
        print(" Previous data loaded successfully!\n")
    else:
        print(" No previous data found. Starting fresh.\n")

#  FUNCTION 2 – Saving data to file
#  Called every time I add/change something
def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=4)    # write students list to file

#  FUNCTION 3 – Adding a new student
#  Uses: dictionary, list.append()
def add_student(name, roll_no):
    # Check if roll number already exists 
    for student in students:
        if student["roll_number"] == roll_no: # to check duplicate roll number
            print(f" Roll number {roll_no} already exists!\n")
            return                          # stop the function

    # Creating a new student dictionary
    new_student = {
        "name"       : name,
        "roll_number": roll_no,
        "marks"      : {}                  # empty dict to add subjects later
    }

    students.append(new_student)           # add to my list
    save_data()                            # save immediately
    print(f" Student '{name}' (Roll No: {roll_no}) added!\n")

#  FUNCTION 4 – Adding marks for a subject
#  Uses: for loop, dictionary, typecasting
def add_marks(roll_no, subject, marks):
    for student in students:
        if student["roll_number"] == roll_no:          # found the student
            student["marks"][subject] = int(marks)     # typecasting to int
            save_data()
            print(f" Marks added: {subject} = {marks} for {student['name']}\n")
            return

    print(f" No student found with Roll No: {roll_no}\n")

#  FUNCTION 5 – Calculating GPA
#  Using if-elif-else
def calculate_gpa(roll_no):
    for student in students:
        if student["roll_number"] == roll_no:

            marks_dict = student["marks"]  # store marks dict

            if len(marks_dict) == 0:       # no marks added yet
                return 0.0

            # Calculate average 
            total = 0
            for subject in marks_dict:
                total = total + marks_dict[subject]  # sum of all marks 

            average = total / len(marks_dict)   # average

            # GPA logic 
            if average > 90:
                gpa = 10.0
            elif average > 80:
                gpa = 9.0
            elif average > 70:
                gpa = 8.0
            elif average > 60:
                gpa = 7.0
            elif average > 50:
                gpa = 6.0
            else:
                gpa = 0.0                  # fail

            return gpa

    return None                            # student not found

#  FUNCTION 6 – Generating report for one student
#  Using for loop, f-strings
def generate_report(roll_no):
    for student in students:
        if student["roll_number"] == roll_no:

            gpa = calculate_gpa(roll_no)      # calls another function

            print("=" * 45)   # create lines (=======)
            print(f"       STUDENT REPORT CARD")
            print("=" * 45)
            print(f"  Name        : {student['name']}")
            print(f"  Roll Number : {student['roll_number']}")
            print("-" * 45)
            print(f"  {'Subject':<20} {'Marks':>10}")   # for formatting (<---left align / >---right align)
            print("-" * 45)

            if len(student["marks"]) == 0:
                print("  No marks added yet.")
            else:
                total = 0
                for subject, marks in student["marks"].items():   # loop through dictonary
                    print(f"  {subject:<20} {marks:>10}")
                    total += marks
                average = total / len(student["marks"])
                print("-" * 45)
                print(f"  {'Average':<20} {average:>10.2f}")
                print(f"  {'GPA':<20} {gpa:>10.1f}")

                if gpa == 0.0:
                    print("  Result:  FAIL")
                else:
                    print("  Result:  PASS")

            print("=" * 45)
            print()
            return

    print(f" No student found with Roll No: {roll_no}\n")

#  FUNCTION 7 – Showing all students
#  Using for loop, f-string
def show_all_students():
    if len(students) == 0:         # no data check
        print(" No students added yet.\n")
        return

    print("=" * 55)
    print(f"  {'Roll No':<10} {'Name':<20} {'Subjects':>10} {'GPA':>8}")
    print("=" * 55)

    for student in students:
        gpa = calculate_gpa(student["roll_number"])
        subject_count = len(student["marks"])
        print(f"  {student['roll_number']:<10} {student['name']:<20} {subject_count:>10} {gpa:>8.1f}")

    print("=" * 55)
    print()

#  FUNCTION 8 – Finding top student
#  Using for loop and if condition
def top_student():
    if len(students) == 0:
        print(" No students to compare.\n")
        return

    best_student = None
    best_gpa     = -1                      # starting with low value

    for student in students:
        gpa = calculate_gpa(student["roll_number"])
        if gpa > best_gpa:                 # if this student has highest GPA
            best_gpa     = gpa
            best_student = student

    print(" TOP STUDENT:")
    print(f"   Name        : {best_student['name']}")
    print(f"   Roll Number : {best_student['roll_number']}")
    print(f"   GPA         : {best_gpa}\n")

#  MAIN MENU  –  while loop 
def main():
    load_data()                            # loading saved data 

    while True:                            # loop for showing same again and again
        print("   STUDENT REPORT CARD SYSTEM     ")
        print("  1. Add Student                  ")
        print("  2. Add Marks                    ")
        print("  3. View Report (one student)    ")
        print("  4. View All Students            ")
        print("  5. Top Student                  ")
        print("  6. Exit                         ")

        choice = input("Enter your choice (1-6): ")   # input is always string

        # Option 1
        if choice == "1":
            name    = input("Enter student name    : ")
            roll_no = input("Enter roll number     : ")
            add_student(name, roll_no)

        # Option 2
        elif choice == "2":
            roll_no = input("Enter roll number     : ")
            subject = input("Enter subject name    : ")
            marks   = input("Enter marks (0-100)   : ")

            # simple validation using typecasting
            if marks.isdigit():     # checking if data is entered or not
                marks = int(marks)
                if 0 <= marks <= 100:      # valid marks
                    add_marks(roll_no, subject, marks)
                else:
                    print(" Marks must be between 0 and 100!\n")
            else:
                print(" Please enter a valid number!\n")

        # Option 3
        elif choice == "3":
            roll_no = input("Enter roll number: ")
            generate_report(roll_no)

        # Option 4
        elif choice == "4":
            show_all_students()

        # Option 5 
        elif choice == "5":
            top_student()

        # Option 6
        elif choice == "6":
            print("Data saved.")
            break                          # exiting the loop

        # Invalid input
        else:
            print(" Invalid choice. Please enter 1 to 6.\n")

if __name__ == "__main__":    # I am using this for running main() only when file is executed directly
    main()
