# Task 1

class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls,student):
        cls.student_list.append(student)
# Task 2
class Student:

    def __init__(self, student_id, name, department, is_enrolled=True):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

        # task 3
        StudentDatabase.add_student(self)

    @property
    def student_id(self):
        return self.__student_id

    
    @property
    def name(self):
        return self.__name  

    @property
    def department(self):
        return self.__department  

    @property
    def is_enrolled(self):
        return self.__is_enrolled


    # task 4
    def enroll_student(self):
        if self.__is_enrolled:
            print( f'Error : Stuent {self.__name} is already enrolled.')
        else:
            self.__is_enrolled = True
            print(f' Student {self.__name} has been enrolled.')

    # task 5

    def drop_student(self):
        if not self.__is_enrolled:
            print(f"Error: Student {self.__name} is not currently enrolled")
        else:
            self.__is_enrolled =False
            print(f"Student {self.__name} has been dropped")
    # task 6

    def view_student_info(self):
        status = "Enrolled" if self.__is_enrolled else "Not Enrolled"
        print(f'ID: {self.__student_id} | Name: {self.__name} | Dept: {self.__department} | Status :{status} ')

  
def find_student(student_id):
    for student in StudentDatabase.student_list:  #[cite: 3]
        if student.student_id == student_id:
            return student
    return None

 #task 7
def main():
    Student(101, "Moni", "Math", True)  
    Student(102, "Toni", "EEE", False)  
    Student(103, "Boni", "CSE", True)  

    while True:
        print("\n--- Student Management System ---")
        print("1. View All Students") 
        print("2. Enroll Student") 
        print("3. Drop Student")  
        print("4. Exit")  

        choice = input("Enter your choice (1-4): ").strip()  

        if choice == "1":
            print("\n--- All Students List ---")
            if not StudentDatabase.student_list:  
                print("No students found.")
            for s in StudentDatabase.student_list:  
                s.view_student_info()  

        elif choice == "2":
            try:
                sid = int(input("Enter Student ID to enroll: "))
                student = find_student(sid)
                if student:
                    student.enroll_student()  
                else:
                    
                    print("Error: Invalid Student ID! Student not found.")
            except ValueError:
                print("Error: Please enter a valid numerical ID.")

        elif choice == "3":
            try:
                sid = int(input("Enter Student ID to drop: "))
                student = find_student(sid)
                if student:
                    student.drop_student()  
                else:
                   
                    print("Error: Invalid Student ID! Student not found.")
            except ValueError:
                print("Error: Please enter a valid numerical ID.")

        elif choice == "4":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please select between 1 and 4.")


if __name__ == "__main__":
    main()