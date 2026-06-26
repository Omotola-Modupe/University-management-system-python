from storage import load_all, save_all


class Department:
    """Manages students, courses, and grades for a department."""

    def __init__(self, name):
        self.name = name
        self.students = {}
        self.courses = {}
        self.grades = []

    def add_student(self, student):
        if student.student_id in self.students:
            raise ValueError(f"Student ID already exists: {student.student_id}")
        self.students[student.student_id] = student

    def add_course(self, course):
        if course.course_code in self.courses:
            raise ValueError(f"Course code already exists: {course.course_code}")
        self.courses[course.course_code] = course

    def assign_grade(self, grade):
        """Assign a grade after verifying the student and course exist."""
        if grade.student_id not in self.students:
            raise KeyError(f"Student not found: {grade.student_id}")
        if grade.course_code not in self.courses:
            raise KeyError(f"Course not found: {grade.course_code}")
        self.grades.append(grade)

    def get_student_report(self, student_id):
        if student_id not in self.students:
            raise KeyError(f"Student not found: {student_id}")

        report = []
        for grade in self.grades:
            if grade.student_id == student_id:
                report.append(grade)
        return report

    def list_students(self):
        if not self.students:
            print("No students registered.")
            return

        for student in self.students.values():
            student.display()

    def list_courses(self):
        if not self.courses:
            print("No courses registered.")
            return

        for course in self.courses.values():
            course.display()

    def load_data(self, data_dir):
        students, courses, grades = load_all(data_dir)
        self.students = students
        self.courses = courses
        self.grades = grades

    def save_data(self, data_dir):
        save_all(data_dir, self)
