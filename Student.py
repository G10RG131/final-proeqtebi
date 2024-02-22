class Student:
    def __init__(self, name, roll_number, grade):
        self.__name = name
        self.__roll_number = roll_number
        self.__grade = grade.upper()

    def get_name(self):
        return self.__name

    def get_roll_number(self):
        return self.__roll_number

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        self.__grade = grade


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_number, grade):
        student = Student(name, roll_number, grade)
        self.students.append(student)
        print("Student added successfully!")

    def show_all_students(self):
        if not self.students:
            print("No students added yet.")
        else:
            print("List of Students:")
            for student in self.students:
                print(f"Name: {student.get_name()}, Roll Number: {student.get_roll_number()}, Grade: {student.get_grade()}")

    def find_student_by_roll_number(self, roll_number):
        found = False
        for student in self.students:
            if str(student.get_roll_number()) == str(roll_number):
                print(f"Student found! Name: {student.get_name()}, Grade: {student.get_grade()}")
                found = True
                break
        if not found:
            print("Student not found.")

    def roll_number_duplicate_check(self, roll_number):
        found = False
        for student in self.students:
            if str(student.get_roll_number()) == str(roll_number):
                found = True
                break
        return found

    def change_grade(self, roll_number, new_grade):
        for student in self.students:
            if str(student.get_roll_number()) == str(roll_number):
                student.set_grade(new_grade)
                print("Grade updated successfully!")
                break
        else:
            print("Student not found.")

    def start(self):
        while True:
            print("\nOptions:")
            print("1. Add new student")
            print("2. Show all students")
            print("3. Find student by roll number")
            print("4. Change grade")
            print("5. End")

            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter student's name: ")
                roll_number = input("Enter student's roll number: ")
                grade = input("Enter student's grade (A-F): ")
                while not roll_number.isnumeric():
                    roll_number = input("Student's roll number must be integer: ")
                while self.roll_number_duplicate_check(roll_number):
                    roll_number = input(f"Student's with {roll_number} number already exists, please provide new number: ")
                while grade.upper() not in ["A", "B", "C", "D", "E", "F"]:
                    grade = input("Student's grade should be from A-F: ")
                self.add_student(name, roll_number, grade)
            elif choice == '2':
                self.show_all_students()
            elif choice == '3':
                roll_number = int(input("Enter student's roll number to find: "))
                self.find_student_by_roll_number(roll_number)
            elif choice == '4':
                roll_number = int(input("Enter student's roll number to change grade: "))
                new_grade = input("Enter new grade: ")
                while new_grade.upper() not in ["A", "B", "C", "D", "E", "F"]:
                    new_grade = input("Student's grade should be from A-F: ")
                self.change_grade(roll_number, new_grade)
            elif choice == '5':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")


# Main program
if __name__ == "__main__":
    system = StudentManagementSystem()
    system.start()
