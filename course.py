class Course:
    """Represents a course offered by the department."""

    def __init__(self, course_code, title, credits, instructor):
        self.course_code = course_code
        self.title = title
        self.credits = int(credits)
        self.instructor = instructor

    def display(self):
        print(
            f"{self.course_code} | {self.title} | "
            f"{self.credits} credits | {self.instructor}"
        )

    def update(self, title=None, credits=None, instructor=None):
        if title:
            self.title = title
        if credits is not None:
            self.credits = int(credits)
        if instructor:
            self.instructor = instructor

    def to_row(self):
        return {
            "course_code": self.course_code,
            "title": self.title,
            "credits": self.credits,
            "instructor": self.instructor,
        }

    @classmethod
    def from_row(cls, row):
        return cls(
            row["course_code"],
            row["title"],
            row["credits"],
            row["instructor"],
        )
