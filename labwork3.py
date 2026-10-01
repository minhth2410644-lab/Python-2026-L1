import math
import numpy as np
import curses

class Student:
    def __init__(self, s_id, name, dob):
        self.id = s_id
        self.name = name
        self.dob = dob
        self.gpa = 0.0

class Course:
    def __init__(self, c_id, name, credits):
        self.id = c_id
        self.name = name
        self.credits = credits

class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {} 

    def input_students(self, stdscr):
        stdscr.clear()
        stdscr.addstr("Input number of students in class: ")
        curses.echo()
        try:
            num = int(stdscr.getstr().decode('utf-8'))
            for _ in range(num):
                stdscr.addstr("Student ID: ")
                s_id = stdscr.getstr().decode('utf-8')
                stdscr.addstr("Student name: ")
                name = stdscr.getstr().decode('utf-8')
                stdscr.addstr("Student DoB: ")
                dob = stdscr.getstr().decode('utf-8')
                self.students.append(Student(s_id, name, dob))
        except ValueError:
            stdscr.addstr("Invalid number!\n")
        curses.noecho()
        stdscr.addstr("\nPress any key to return...")
        stdscr.getch()

    def input_courses(self, stdscr):
        stdscr.clear()
        stdscr.addstr("Input number of courses: ")
        curses.echo()
        try:
            num = int(stdscr.getstr().decode('utf-8'))
            for _ in range(num):
                stdscr.addstr("Course ID: ")
                c_id = stdscr.getstr().decode('utf-8')
                stdscr.addstr("Course name: ")
                name = stdscr.getstr().decode('utf-8')
                stdscr.addstr("Course credits (for GPA): ")
                credits = int(stdscr.getstr().decode('utf-8'))
                self.courses.append(Course(c_id, name, credits))
        except ValueError:
            stdscr.addstr("Invalid input!\n")
        curses.noecho()
        stdscr.addstr("\nPress any key to return...")
        stdscr.getch()

    def input_marks(self, stdscr):
        stdscr.clear()
        if not self.courses or not self.students:
            stdscr.addstr("Add students and courses first.\nPress any key...")
            stdscr.getch()
            return

        stdscr.addstr("Select a course ID to input marks: ")
        curses.echo()
        c_id = stdscr.getstr().decode('utf-8')
        
        if c_id not in [c.id for c in self.courses]:
            stdscr.addstr("Invalid course ID.\nPress any key...")
            curses.noecho()
            stdscr.getch()
            return

        if c_id not in self.marks:
            self.marks[c_id] = {}

        for s in self.students:
            stdscr.addstr(f"Input mark for student {s.name}: ")
            try:
                mark = float(stdscr.getstr().decode('utf-8'))
                # Round down to 1-digit decimal using math.floor
                mark = math.floor(mark * 10) / 10.0
                self.marks[c_id][s.id] = mark
            except ValueError:
                stdscr.addstr("Invalid mark! Skipping...\n")

        curses.noecho()
        stdscr.addstr("\nMarks saved. Press any key...")
        stdscr.getch()

    def calculate_gpa_and_sort(self):
        for s in self.students:
            marks_list = []
            credits_list = []
            for c in self.courses:
                if c.id in self.marks and s.id in self.marks[c.id]:
                    marks_list.append(self.marks[c.id][s.id])
                    credits_list.append(c.credits)
            
            if marks_list:
                m_arr = np.array(marks_list)
                c_arr = np.array(credits_list)
                # Weighted sum of credits and marks using numpy
                s.gpa = np.sum(m_arr * c_arr) / np.sum(c_arr)
            else:
                s.gpa = 0.0
                
        # Sort descending by GPA
        self.students.sort(key=lambda x: x.gpa, reverse=True)

    def list_students(self, stdscr):
        stdscr.clear()
        self.calculate_gpa_and_sort()
        stdscr.addstr("--- Student List (Sorted by GPA) ---\n")
        for s in self.students:
            stdscr.addstr(f"ID: {s.id} | Name: {s.name} | DoB: {s.dob} | GPA: {s.gpa:.1f}\n")
        stdscr.addstr("\nPress any key to return...")
        stdscr.getch()

    def show_marks(self, stdscr):
        stdscr.clear()
        stdscr.addstr("Input course ID to show marks: ")
        curses.echo()
        c_id = stdscr.getstr().decode('utf-8')
        curses.noecho()

        if c_id in self.marks:
            stdscr.addstr(f"\n--- Marks for Course {c_id} ---\n")
            for s in self.students:
                mark = self.marks[c_id].get(s.id, 'No mark yet')
                stdscr.addstr(f"Student {s.name}: {mark}\n")
        else:
            stdscr.addstr("No mark data for this course.\n")

        stdscr.addstr("\nPress any key to return...")
        stdscr.getch()

def main(stdscr):
    school = School()
    while True:
        stdscr.clear()
        stdscr.addstr("--- USTH Student Mark Management ---\n")
        stdscr.addstr("1. Input Students\n")
        stdscr.addstr("2. Input Courses\n")
        stdscr.addstr("3. Input Marks\n")
        stdscr.addstr("4. List Students (Sorted by GPA)\n")
        stdscr.addstr("5. Show Marks\n")
        stdscr.addstr("6. Quit\n")
        stdscr.addstr("Select an option: ")
        
        curses.echo()
        choice = stdscr.getstr().decode('utf-8')
        curses.noecho()

        if choice == '1':
            school.input_students(stdscr)
        elif choice == '2':
            school.input_courses(stdscr)
        elif choice == '3':
            school.input_marks(stdscr)
        elif choice == '4':
            school.list_students(stdscr)
        elif choice == '5':
            school.show_marks(stdscr)
        elif choice == '6':
            break

if __name__ == "__main__":
    curses.wrapper(main)