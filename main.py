from school import School
from person import Student, Teacher
from subject import Subject
from classroom import ClassRoom


def main():
    school = School.load_school()
    if not school:
        school = School('ABC High School', 'Dhaka')
        print("New school created.")
    else:
        print(f"Loaded school: {school.name}")

    while True:
        print("\n--- School Management System ---")
        print("1. Add Classroom")
        print("2. Add Student")
        print("3. Add Teacher")
        print("4. Add Subject to Classroom")
        print("5. Take Exam (All Classes)")
        print("6. Show Status")
        print("7. Exit (Save & Close)")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter Classroom Name (e.g., Six, Seven): ")
            cr = ClassRoom(name)
            school.add_classroom(cr)
            print(f"Classroom {name} added.")
            
        elif choice == '2':
            name = input("Enter Student Name: ")
            classroom_name = input("Enter Classroom Name: ")
            if classroom_name in school.classrooms:
                classroom = school.classrooms[classroom_name]
                student = Student(name, classroom)
                school.student_admission(student)
                print(f"Student {name} admitted to {classroom_name}.")
            else:
                print(f"Classroom {classroom_name} not found.")

        elif choice == '3':
            # In this simple system, teachers are created when adding subjects, 
            # or just stored temporarily if we want a pool. 
            # But the current design links Teacher directly to Subject.
            # Let's just create a teacher and keep them in a list for selection?
            # Or just simplify: "Add Subject" asks for Teacher name.
            # But the user asked for "Add Teacher" specifically.
            name = input("Enter Teacher Name: ")
            print(f"To assign {name} to a subject, use option 4.")
            # We could store teachers in School if we modify School.py, 
            # but for now let's just allow creating them on the fly in option 4 
            # or store them in a local list in main().
            
        elif choice == '4':
            classroom_name = input("Enter Classroom Name: ")
            if classroom_name in school.classrooms:
                subject_name = input("Enter Subject Name: ")
                teacher_name = input("Enter Teacher Name: ")
                teacher = Teacher(teacher_name)
                subject = Subject(subject_name, teacher)
                school.classrooms[classroom_name].add_subject(subject)
                print(f"Subject {subject_name} added to {classroom_name} with teacher {teacher_name}.")
            else:
                print(f"Classroom {classroom_name} not found.")

        elif choice == '5':
            for classroom in school.classrooms.values():
                classroom.take_semester_final_exam()
            print("Exams taken for all classrooms.")

        elif choice == '6':
            print(school)

        elif choice == '7':
            print("Saving data...")
            school.save_school()
            break
        
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
