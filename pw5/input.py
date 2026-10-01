import curses
import math
from domains.student import Student
from domains.course import Course

def input_students(stdscr, students):
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
            students.append(Student(s_id, name, dob))
    except ValueError:
        stdscr.addstr("Invalid number!\n")
    curses.noecho()
    stdscr.addstr("\nPress any key to return...")
    stdscr.getch()

def input_courses(stdscr, courses):
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
            courses.append(Course(c_id, name, credits))
    except ValueError:
        stdscr.addstr("Invalid input!\n")
    curses.noecho()
    stdscr.addstr("\nPress any key to return...")
    stdscr.getch()

def input_marks(stdscr, students, courses, marks):
    stdscr.clear()
    if not courses or not students:
        stdscr.addstr("Add students and courses first.\nPress any key...")
        stdscr.getch()
        return

    stdscr.addstr("Select a course ID to input marks: ")
    curses.echo()
    c_id = stdscr.getstr().decode('utf-8')
    
    if c_id not in [c.id for c in courses]:
        stdscr.addstr("Invalid course ID.\nPress any key...")
        curses.noecho()
        stdscr.getch()
        return

    if c_id not in marks:
        marks[c_id] = {}

    for s in students:
        stdscr.addstr(f"Input mark for student {s.name}: ")
        try:
            mark = float(stdscr.getstr().decode('utf-8'))
            mark = math.floor(mark * 10) / 10.0
            marks[c_id][s.id] = mark
        except ValueError:
            stdscr.addstr("Invalid mark! Skipping...\n")

    curses.noecho()
    stdscr.addstr("\nMarks saved. Press any key...")
    stdscr.getch()