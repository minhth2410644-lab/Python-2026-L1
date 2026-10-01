import input as in_mod
import output as out_mod
from domains.student import Student
from domains.course import Course

def main():
    students = []
    courses = []

    num_students = in_mod.input_number_of_students()
    for _ in range(num_students):
        sid, name, dob = in_mod.input_student_info()
        students.append(Student(sid, name, dob))

    num_courses = in_mod.input_number_of_courses()
    for _ in range(num_courses):
        cid, name, credit = in_mod.input_course_info()
        courses.append(Course(cid, name, credit))

    for course in courses:
        in_mod.input_marks_for_course(students, course)

    for student in students:
        student.calculate_gpa(courses)

    gpas = np.array([s.gpa for s in students])
    sorted_indices = np.argsort(gpas)[::-1]
    students = [students[i] for i in sorted_indices]

    out_mod.list_courses(courses)
    out_mod.list_students(students)

if __name__ == "__main__":
    main()