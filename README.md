# CS Department System

A simple menu-driven Python application for managing students, courses, and grades in a university Computer Science department. Data is stored in CSV files.

Clone or download this repository, then open a terminal in the project folder.

## Example Usage

```
=== CS Department System ===
1. Add student
2. Add course
3. Assign grade
4. View student report
5. List all students
6. List all courses
7. Save and exit
0. Exit without saving
Choose an option: 4
Student ID: S001

Report for Alice Johnson (S001)
CS101 - Introduction to Programming: 88.0 (B)
```

To persist changes, choose option **7** before exiting.

## Key Features

- Add and list students
- Add and list courses
- Assign grades with automatic letter-grade conversion
- View a grade report for any student
- Save and load data from CSV files
- Input validation and error handling

## Project Files

| File | Description |
|------|-------------|
| `main.py` | Entry point and interactive menu |
| `department.py` | Department class that coordinates records |
| `student.py` | Student model |
| `course.py` | Course model |
| `grade.py` | Grade model with letter-grade logic |
| `storage.py` | CSV load/save helpers |
| `data/students.csv` | Sample student records |
| `data/courses.csv` | Sample course records |
| `data/grades.csv` | Sample grade records |

