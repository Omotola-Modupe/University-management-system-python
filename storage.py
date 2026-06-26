import csv
from pathlib import Path

from course import Course
from grade import Grade
from student import Student

STUDENT_FIELDS = ["student_id", "name", "email"]
COURSE_FIELDS = ["course_code", "title", "credits", "instructor"]
GRADE_FIELDS = ["student_id", "course_code", "score", "letter"]


def load_csv(filepath):
    """Read rows from a CSV file, returning an empty list if missing."""
    path = Path(filepath)
    if not path.exists():
        return []

    try:
        with path.open(newline="", encoding="utf-8") as handle:
            return list(csv.DictReader(handle))
    except FileNotFoundError:
        return []


def save_csv(filepath, rows, fieldnames):
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def load_all(data_dir):
    """Load students, courses, and grades from the data directory."""
    base = Path(data_dir)

    student_rows = load_csv(base / "students.csv")
    course_rows = load_csv(base / "courses.csv")
    grade_rows = load_csv(base / "grades.csv")

    students = {row["student_id"]: Student.from_row(row) for row in student_rows}
    courses = {row["course_code"]: Course.from_row(row) for row in course_rows}
    grades = [Grade.from_row(row) for row in grade_rows]

    return students, courses, grades


def save_all(data_dir, department):
    base = Path(data_dir)

    save_csv(
        base / "students.csv",
        [student.to_row() for student in department.students.values()],
        STUDENT_FIELDS,
    )
    save_csv(
        base / "courses.csv",
        [course.to_row() for course in department.courses.values()],
        COURSE_FIELDS,
    )
    save_csv(
        base / "grades.csv",
        [grade.to_row() for grade in department.grades],
        GRADE_FIELDS,
    )
