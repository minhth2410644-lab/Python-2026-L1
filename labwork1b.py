
students = []  # [{ "id": ..., "name": ..., "dob": ... }]
courses = []   # [{ "id": ..., "name": ... }]
marks = {}     # { course_id: { student_id: mark } }

def input_number_of_students():
    return int(input("Enter number of students: "))

def input_students():
    num_students = input_number_of_students()
    for _ in range(num_students):
        print(f"\n--- Input Student {len(students) + 1} ---")
        sid = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        dob = input("Enter Date of Birth (DoB): ")
        students.append({"id": sid, "name": name, "dob": dob})

def input_number_of_courses():
    return int(input("Enter number of courses: "))

def input_courses():
    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        print(f"\n--- Input Course {len(courses) + 1} ---")
        cid = input("Enter Course ID: ")
        name = input("Enter Course Name: ")
        courses.append({"id": cid, "name": name})

def input_marks():
    if not courses:
        print("No courses available! Please add courses first.")
        return
    if not students:
        print("No students available! Please add students first.")
        return

    print("\n--- Select Course to Input Marks ---")
    list_courses()
    cid = input("Enter Course ID: ")
    
    course_exists = any(c['id'] == cid for c in courses)
    if not course_exists:
        print("Course ID not found!")
        return

    if cid not in marks:
        marks[cid] = {}

    print(f"\nEntering marks for course: {cid}")
    for s in students:
        score = float(input(f"Enter mark for {s['name']} (ID: {s['id']}): "))
        marks[cid][s['id']] = score

def list_courses():
    print("\n=== COURSE LIST ===")
    if not courses:
        print("No courses available.")
        return
    for c in courses:
        print(f"ID: {c['id']} | Name: {c['name']}")

def list_students():
    print("\n=== STUDENT LIST ===")
    if not students:
        print("No students available.")
        return
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | DoB: {s['dob']}")

def show_student_marks():
    cid = input("\nEnter Course ID to view marks: ")
    if cid not in marks or not marks[cid]:
        print("No marks found for this course!")
        return

    print(f"\n=== MARKS FOR COURSE: {cid} ===")
    for s in students:
        sid = s['id']
        if sid in marks[cid]:
            print(f"ID: {sid} | Name: {s['name']} | Mark: {marks[cid][sid]}")

def main():
    while True:
        print("\n=================================")
        print(" STUDENT MARK MANAGEMENT SYSTEM ")
        print("=================================")
        print("1. Input students")
        print("2. Input courses")
        print("3. Select course and input marks")
        print("4. List courses")
        print("5. List students")
        print("6. Show student marks for a course")
        print("0. Exit")
        
        choice = input("Enter option (0-6): ")
        
        if choice == '1':
            input_students()
        elif choice == '2':
            input_courses()
        elif choice == '3':
            input_marks()
        elif choice == '4':
            list_courses()
        elif choice == '5':
            list_students()
        elif choice == '6':
            show_student_marks()
        elif choice == '0':
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please try again!")

if __name__ == "__main__":
    main()