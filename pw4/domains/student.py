class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {} 
        self.gpa = 0.0

    def calculate_gpa(self, courses):
        total_credits = 0
        weighted_sum = 0
        for course in courses:
            if course.id in self.marks:
                weighted_sum += self.marks[course.id] * course.credit
                total_credits += course.credit

        if total_credits > 0:
            self.gpa = round(weighted_sum / total_credits, 2)
        else:
            self.gpa = 0.0
        return self.gpa