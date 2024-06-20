def get_student_details():
    students = {}
    n = int(input("Enter the number of students: "))

    for _ in range(n):      #The underscore _ signifies that the loop variable is not used in the body of the loop. The focus is on executing the loop body (collecting and storing student details) n times.
        roll_no = input("Enter roll number: ")
        name = input("Enter the name: ")
        total_mark = int(input("Enter the total marks: "))
        students[roll_no] = {'name': name, 'total_mark': total_mark}

    return students

def find_top_student(students):
    top_student = None
    highest_mark = -1

    for roll_no, details in students.items():
        if details['total_mark'] > highest_mark:
            highest_mark = details['total_mark']
            top_student = (roll_no, details)

    return top_student

# Get student details
students = get_student_details()

# Find and print the top student
top_student = find_top_student(students)

if top_student:
    roll_no, details = top_student
    print("\nDetails of the student with the highest total marks:")
    print(f"Roll Number: {roll_no}")
    print(f"Name: {details['name']}")
    print(f"Total Marks: {details['total_mark']}")
else:
    print("No student details available.")
