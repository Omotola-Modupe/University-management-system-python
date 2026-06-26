class Grade:
    """Represents a grade assigned to a student for a course."""

    def __init__(self, student_id, course_code, score):
        self.student_id = student_id
        self.course_code = course_code
        self.score = float(score)
        self.letter = self.to_letter(self.score)

    @staticmethod
    def to_letter(score):
        """Convert a numeric score to a letter grade."""
        if score >= 90:
            return "A"
        if score >= 80:
            return "B"
        if score >= 70:
            return "C"
        if score >= 60:
            return "D"
        return "F"

    def update_score(self, score):
        """Update the numeric score and recalculate the letter grade."""
        self.score = float(score)
        self.letter = self.to_letter(self.score)

    def display(self):
        print(
            f"{self.student_id} | {self.course_code} | {self.score:.1f} ({self.letter})"
        )

    def to_row(self):
        return {
            "student_id": self.student_id,
            "course_code": self.course_code,
            "score": self.score,
            "letter": self.letter,
        }

    @classmethod
    def from_row(cls, row):
        grade = cls(row["student_id"], row["course_code"], row["score"])
        grade.letter = row["letter"]
        return grade
