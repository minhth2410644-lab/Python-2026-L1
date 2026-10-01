def list_students(students):
    print("\n=== STUDENT LIST (Sorted by GPA) ===")
    for student in students:
        print(f"ID: {student.id} | Name: {student.name} | DoB: {student.dob} | GPA: {student.gpa}")

def list_courses(courses):
    print("\n=== COURSE LIST ===")
    for course in courses:
        print(f"ID: {course.id} | Name: {course.name} | Credit: {course.credit}")