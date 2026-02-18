# School Management System

A Python-based CLI application that demonstrates Object-Oriented Programming (OOP) principles through a School Management System simulation.

## Features

- **Interactive CLI**: Menu-driven interface to manage school operations.
- **Manage Classrooms**: Add new classrooms (e.g., Six, Seven, Eight).
- **Student Admission**: Admit students to specific classrooms.
- **Teacher Management**: Assign teachers to subjects.
- **Subject Allocation**: Add subjects to classrooms with assigned teachers.
- **Examination System**: Take semester final exams for all classes.
- **Grading System**: Automated grade calculation based on marks.
- **Data Persistence**: School data is automatically saved and loaded (`school_data.pkl`), so you don't lose your progress.
- **Reporting**: View detailed text reports of students, subjects, and exam results.

## Project Structure

- `main.py`: The entry point of the application, handling the CLI menu and user interaction.
- `school.py`: Contains the `School` class which manages classrooms, teachers, and overall school operations. Includes persistence logic.
- `person.py`: Defines the `Person` base class and `Student`/`Teacher` subclasses.
- `classroom.py`: Manages classroom-specific data like students and subjects.
- `subject.py`: Handles subject details and exam evaluation.

## How to Run

1.  Make sure you have Python installed.
2.  Clone the repository:
    ```bash
    git clone https://github.com/Azmine-Zim/school-management-system.git
    cd school-management-system
    ```
3.  Run the main script:
    ```bash
    python main.py
    ```
4.  Follow the on-screen menu to manage your school system.

## OOP Concepts Used

- **Inheritance**: `Student` and `Teacher` inherit from `Person`.
- **Encapsulation**: Used for ID generation and property management.
- **Polymorphism**: Demonstrates flexible object interactions.
- **Composition**: Relationships between `School`, `ClassRoom`, and `Subject`.
