from pathlib import Path

from course import Course
from department import Department
from grade import Grade
from student import Student

DATA_DIR = Path(__file__).parent / "data"


def print_menu():
    """Display the main menu."""
    print("""\n=== CS Department System ===
    
    1. Add student
    2. Add course
    3. Assign grade
    4. View student report
    5. List all students
    6. List all courses
    7. Save and exit
    0. Exit without saving
    """)


def prompt_add_student(department):
    """Prompt for student details and add to the department."""
    student_id = input("Student ID: ").strip()
    name = input("Name: ").strip()
    email = input("Email: ").strip()

    if not student_id or not name or not email:
        raise ValueError("All student fields are required.")

    department.add_student(Student(student_id, name, email))
    print("Student added.")


def add_course(department):
    course_code = input("Course code: ").strip()
    title = input("Title: ").strip()
    credits = input("Credits: ").strip()
    instructor = input("Instructor: ").strip()

    if not course_code or not title or not instructor:
        raise ValueError("Course code, title, and instructor are required.")

    try:
        credits_value = int(credits)
    except ValueError as exc:
        raise ValueError("Credits must be a whole number.") from exc

    department.add_course(Course(course_code, title, credits_value, instructor))
    print("Course added.")


def assign_grade(department):
    student_id = input("Student ID: ").strip()
    course_code = input("Course code: ").strip()
    score = input("Score (0-100): ").strip()

    try:
        score_value = float(score)
    except ValueError as exc:
        raise ValueError("Score must be a number.") from exc

    if score_value < 0 or score_value > 100:
        raise ValueError("Score must be between 0 and 100.")

    department.assign_grade(Grade(student_id, course_code, score_value))
    print("Grade assigned.")


def get_student_report(department):
    student_id = input("Student ID: ").strip()
    grades = department.get_student_report(student_id)
    student = department.students[student_id]

    print(f"\nReport for {student.name} ({student_id})")
    if not grades:
        print("No grades recorded.")
        return

    for grade in grades:
        course = department.courses[grade.course_code]
        print(
            f"{course.course_code} - {course.title}: {grade.score:.1f} ({grade.letter})"
        )


def main():
    department = Department("Computer Science")
    department.load_data(DATA_DIR)

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                prompt_add_student(department)
            elif choice == "2":
                add_course(department)
            elif choice == "3":
                assign_grade(department)
            elif choice == "4":
                get_student_report(department)
            elif choice == "5":
                department.list_students()
            elif choice == "6":
                department.list_courses()
            elif choice == "7":
                department.save_data(DATA_DIR)
                print("Data saved. Goodbye.")
                break
            elif choice == "0":
                print("Goodbye.")
                break
            else:
                print("Invalid option. Please try again.")
        except ValueError as exc:
            print(f"Error: {exc}")
        except KeyError as exc:
            message = exc.args[0] if exc.args else exc
            print(f"Error: {message}")
        except FileNotFoundError:
            print("Error: Data file not found.")


if __name__ == "__main__":
    main()
