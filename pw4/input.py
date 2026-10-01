import math

def input_number_of_students():
    return int(input("Enter number of students: "))

def input_student_info():
    student_id = input("Student ID: ")
    name = input("Student Name: ")
    dob = input("DoB (DD/MM/YYYY): ")
    return student_id, name, dob

def input_number_of_courses():
    return int(input("Enter number of courses: "))

def input_course_info():
    course_id = input("Course ID: ")
    name = input("Course Name: ")
    credit = int(input("Credits: "))
    return course_id, name, credit

def input_marks_for_course(students, course):
    print(f"\n--- Enter marks for course: {course.name} ---")
    for student in students:
        mark = float(input(f"Mark for {student.name} (ID: {student.id}): "))
        rounded_mark = math.floor(mark * 10) / 10.0
        student.marks[course.id] = rounded_mark