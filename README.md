# School Management System

A Python-based CLI application that demonstrates Object-Oriented Programming (OOP) principles through a School Management System simulation.

## Features

- **Manage Classrooms**: Add new classrooms (e.g., Six, Seven, Eight).
- **Student Admission**: Admit students to specific classrooms.
- **Teacher Management**: Assign teachers to subjects.
- **Subject Allocation**: Add subjects to classrooms with assigned teachers.
- **Examination System**: functionality to take semester final exams for all classes.
- **Grading System**: Automated grade calculation based on marks.
- **Data Persistence**: School data is automatically saved and loaded, so you don't lose your progress.
- **Reporting**: View detailed reports of students, subjects, and exam results.

## Project Structure

- `main.py`: The entry point of the application, handling the CLI menu and user interaction.
- `school.py`: Contains the `School` class which manages classrooms, teachers, and overall school operations.
- `person.py`: Defines the `Person` base class and `Student`/`Teacher` subclasses.
- `classroom.py`: Manages classroom-specific data like students and subjects.
- `subject.py`: Handles subject details and exam evaluation.

## How to Run

1.  Make sure you have Python installed.
2.  Run the main script:

    ```bash
    python main.py
    ```

3.  Follow the on-screen menu to manage your school system.

## Requirements

- Python 3.x

## OOP Concepts Used

- **Inheritance**: `Student` and `Teacher` inherit from `Person`.
- **Encapsulation**: Private attributes and property decorators.
- **Polymorphism**: Method overriding and flexible object interactions.
- **Composition**: relationships between `School`, `ClassRoom`, and `Subject`.
