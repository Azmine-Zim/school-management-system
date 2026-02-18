import pickle

class School:
    def __init__(self,name,address):
        self.name=name
        self.address=address
        self.teachers={}
        self.classrooms={}
    def add_classroom(self,classroom):
        self.classrooms[classroom.name]=classroom
    def add_teacher(self,subject,teacher):
        self.teachers[subject]=teacher
    def student_admission(self,student):
        classname=student.classroom.name
        if classname in self.classrooms:
            self.classrooms[classname].add_student(student)
        else:
            print(f"Error: Classroom {classname} not found")

    def save_school(self, filename='school_data.pkl'):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
        print(f"School data saved to {filename}")

    @staticmethod
    def load_school(filename='school_data.pkl'):
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return None

    @staticmethod
    def calculate_grade(marks):
        if marks>=80 and marks<=100:
            return 'A+'
        elif marks>=70 and marks<80:
            return 'A-'
        elif marks>=60 and marks<70:
            return 'B'
        elif marks>=50 and marks<60:
            return 'C+'
        elif marks>=40 and marks<50:
            return 'C'
        elif marks>=33 and marks<40:
            return 'D'
        else:
            return 'F'
        
    @staticmethod
    def grade_to_value(grade):
        grade_map={
            'A+': 5.00,
            'A' : 4.00,
            'A-' : 3.50,
            'B' : 3.00,
            'C+' : 2.50,
            'C' : 2.00,
            'D' : 1.00,
            'F' : 0.00
        }
        return grade_map[grade]
    @staticmethod
    def value_to_grade(value):
        if value>=4.5 and value<=5.00:
            return 'A+'
        elif value>=3.5 and value<4.50:
            return 'A'
        elif value>=3.0 and value<3.5:
            return 'A-'
        elif value>=2.5 and value<3.0:
            return 'B'        
        elif value>=2.25 and value<2.5:
            return 'C+'
        elif value>=2.0 and value<2.25:
            return 'C'      
        elif value>=1.0 and value<2.0:
            return 'D'
        else:
            return 'F'
    
    def __str__(self):
        output = [f"\n=== School: {self.name} ===", "--- Classrooms ---"]
        for key in self.classrooms.keys():
            output.append(key)
        
        output.append("\n--- Students ---")
        for key, value in self.classrooms.items():
            if value.students:
                output.append(f"Classroom {key.upper()}:")
                for student in value.students:
                    output.append(f"  - {student.name}")
        
        output.append("\n--- Subjects ---")
        for key, value in self.classrooms.items():
            if value.subjects:
                output.append(f"Classroom {key.upper()}:")
                for sub in value.subjects:
                    if hasattr(sub, 'teacher') and sub.teacher:
                        t_name = sub.teacher.name
                    else:
                         t_name = 'None'
                    output.append(f"  - {sub.name} (Teacher: {t_name})")

        output.append("\n--- Exam Results ---")
        for key, value in self.classrooms.items():
            for student in value.students:
                if hasattr(student, 'marks') and student.marks:
                     output.append(f"Student: {student.name}")
                     for k, i in student.marks.items():
                        grade = student.subject_grade.get(k, 'N/A')
                        output.append(f"    {k}: {i} ({grade})")
                     output.append(f"    Final: {student.calculate_final_grade()}")
                else:
                    output.append(f"Student: {student.name} (No marks)")
                    
        return '\n'.join(output)

    def __repr__(self):
        for key in self.classrooms.keys():
            print(key)
        print('All Students')
        result=''
        for key,value in self.classrooms.items():
            result+=f'---{key.upper()} Classroom Students\n'
            for student in value.students:
                result +=f'{student.name}\n'
        print(result)

        subject=''
        for key,value in self.classrooms.items():
            subject+=f'---{key.upper()} Classroom Subjects\n'
            for sub in value.subjects:
                subject +=f'{sub.name}\n'
        print(subject)

        print('Student Results')
        for key,value in self.classrooms.items():
            for student in value.students:
                for k,i in student.marks.items():
                    print(student.name,k,i,student.subject_grade[k])
                print(student.calculate_final_grade())
        return ''    