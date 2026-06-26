class Student:
    """Represents a student enrolled in the department."""

    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email

    def display(self):
        print(f"{self.student_id} | {self.name} | {self.email}")

    def update(self, name=None, email=None):
        if name:
            self.name = name
        if email:
            self.email = email

    def to_row(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "email": self.email,
        }

    @classmethod
    def from_row(cls, row):
        return cls(row["student_id"], row["name"], row["email"])
