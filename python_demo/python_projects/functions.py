students = {}
# Add Student
def add_student():
    roll = input("Enter Roll Number: ")
    if roll in students:
        print("Student already exists!")
    name = input("Enter Name: ")
    CGP = float(input("Enter Student CGP: "))
    students[roll] = {"name": name,"CGP": CGP}
    print("Student Added Successfully!")
# View Students
def view_students():
    if not students:
        print("No student records found.")
    print("\n--- Student Records ---")
    for roll, data in students.items():
        print(f"Roll No: {roll}")
        print(f"Name   : {data['name']}")
        print(f"CGP  : {data['CGP']}")
        print("----------------------")
# Search Student
def find_student():
    roll = input("Enter Roll Number to Search: ")
    if roll in students:
        print("\nStudent Found")
        print("Name :", students[roll]["name"])
        print("CGP:", students[roll]["CGP"])
    else:
        print("Student not found!")
# Update Student
def update_student():
    roll = input("Enter Roll Number to Update: ")
    if roll in students:
        name = input("Enter New Name: ")
        CGP = float(input("Update CGP: "))
        students[roll]["name"] = name
        students[roll]["CGP"] = CGP
        print("Student Updated Successfully!")
    else:
        print("Student not found!")
# Delete Student
def delete_student():
    roll = input("Enter Roll Number to Delete: ")
    if roll in students:
        del students[roll]
        print("Student Deleted Successfully!")
    else:
        print("Student not found!")
# Main Menu
def menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Find Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            find_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting Program...")
            break
        else:
            print("Invalid Choice! Try Again.")
# Run Program
menu()