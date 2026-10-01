import curses
import os
import zipfile
import input
import output
from domains.student import Student
from domains.course import Course

def save_data(students, courses, marks):
    save_dir = os.path.dirname(os.path.abspath(__file__))
    
    students_txt = os.path.join(save_dir, "students.txt")
    courses_txt = os.path.join(save_dir, "courses.txt")
    marks_txt = os.path.join(save_dir, "marks.txt")
    dat_file = os.path.join(save_dir, "students.dat")

    with open(students_txt, "w") as f:
        for s in students:
            f.write(f"{s.id},{s.name},{s.dob}\n")
    
    with open(courses_txt, "w") as f:
        for c in courses:
            f.write(f"{c.id},{c.name},{c.credits}\n")
            
    with open(marks_txt, "w") as f:
        for c_id, s_marks in marks.items():
            for s_id, mark in s_marks.items():
                f.write(f"{c_id},{s_id},{mark}\n")
                
    with zipfile.ZipFile(dat_file, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(students_txt, arcname="students.txt")
        zipf.write(courses_txt, arcname="courses.txt")
        zipf.write(marks_txt, arcname="marks.txt")
        
    os.remove(students_txt)
    os.remove(courses_txt)
    os.remove(marks_txt)

def load_data(students, courses, marks):
    save_dir = os.path.dirname(os.path.abspath(__file__))
    dat_file = os.path.join(save_dir, "students.dat")
    
    if os.path.exists(dat_file):
        with zipfile.ZipFile(dat_file, "r") as zipf:
            zipf.extractall(path=save_dir)
            
        students_txt = os.path.join(save_dir, "students.txt")
        courses_txt = os.path.join(save_dir, "courses.txt")
        marks_txt = os.path.join(save_dir, "marks.txt")
            
        if os.path.exists(students_txt):
            with open(students_txt, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        students.append(Student(parts[0], parts[1], parts[2]))
            os.remove(students_txt)
            
        if os.path.exists(courses_txt):
            with open(courses_txt, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        courses.append(Course(parts[0], parts[1], int(parts[2])))
            os.remove(courses_txt)
            
        if os.path.exists(marks_txt):
            with open(marks_txt, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        c_id, s_id, mark = parts[0], parts[1], float(parts[2])
                        if c_id not in marks:
                            marks[c_id] = {}
                        marks[c_id][s_id] = mark
            os.remove(marks_txt)

def main(stdscr):
    students = []
    courses = []
    marks = {}
    load_data(students, courses, marks)

    while True:
        stdscr.clear()
        stdscr.addstr("--- USTH Student Mark Management (PW5) ---\n")
        stdscr.addstr("1. Input Students\n")
        stdscr.addstr("2. Input Courses\n")
        stdscr.addstr("3. Input Marks\n")
        stdscr.addstr("4. List Students (Sorted by GPA)\n")
        stdscr.addstr("5. Show Marks\n")
        stdscr.addstr("6. Quit & Save Data\n")
        stdscr.addstr("Select an option: ")
        
        curses.echo()
        choice = stdscr.getstr().decode('utf-8')
        curses.noecho()

        if choice == '1':
            input.input_students(stdscr, students)
        elif choice == '2':
            input.input_courses(stdscr, courses)
        elif choice == '3':
            input.input_marks(stdscr, students, courses, marks)
        elif choice == '4':
            output.list_students(stdscr, students, courses, marks)
        elif choice == '5':
            output.show_marks(stdscr, students, marks)
        elif choice == '6':
            # Compress and save data before exiting
            save_data(students, courses, marks)
            break

if __name__ == "__main__":
    curses.wrapper(main)