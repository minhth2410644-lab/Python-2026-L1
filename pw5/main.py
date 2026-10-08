import curses
import os
import zipfile
import pickle
import pandas as pd
import input
import output

def save_and_export_data(students, courses, marks):
    save_dir = os.path.dirname(os.path.abspath(__file__))
    
    pkl_path = os.path.join(save_dir, "data.pkl")
    with open(pkl_path, "wb") as f:
        pickle.dump((students, courses, marks), f)
        
    dat_file = os.path.join(save_dir, "students.dat")
    with zipfile.ZipFile(dat_file, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(pkl_path, arcname="data.pkl")
    os.remove(pkl_path)
    
    std_csv = os.path.join(save_dir, "students.csv")
    crs_csv = os.path.join(save_dir, "courses.csv")
    mrk_csv = os.path.join(save_dir, "marks.csv")
    
    with open(std_csv, "w", encoding="utf-8") as f:
        f.write("id,name,dob\n")
        for s in students: f.write(f"{s.id},{s.name},{s.dob}\n")
        
    with open(crs_csv, "w", encoding="utf-8") as f:
        f.write("id,name,credits\n")
        for c in courses: f.write(f"{c.id},{c.name},{c.credits}\n")
        
    with open(mrk_csv, "w", encoding="utf-8") as f:
        f.write("course_id,student_id,mark\n")
        for c_id, s_marks in marks.items():
            for s_id, mark in s_marks.items():
                f.write(f"{c_id},{s_id},{mark}\n")

def load_data(students, courses, marks):
    save_dir = os.path.dirname(os.path.abspath(__file__))
    dat_file = os.path.join(save_dir, "students.dat")
    
    if os.path.exists(dat_file):
        with zipfile.ZipFile(dat_file, "r") as zipf:
            zipf.extract("data.pkl", path=save_dir)
        
        pkl_path = os.path.join(save_dir, "data.pkl")
        if os.path.exists(pkl_path):
            with open(pkl_path, "rb") as f:
                loaded_s, loaded_c, loaded_m = pickle.load(f)
                students.extend(loaded_s)
                courses.extend(loaded_c)
                marks.update(loaded_m)
            os.remove(pkl_path)

def pandas_query(stdscr):
    stdscr.clear()
    save_dir = os.path.dirname(os.path.abspath(__file__))
    std_csv = os.path.join(save_dir, "students.csv")
    
    if not os.path.exists(std_csv):
        stdscr.addstr("CSV file not found. Select (6) to export data first.\nPress any key...")
        stdscr.getch()
        return
        
    try:
        df_students = pd.read_csv(std_csv)
        stdscr.addstr("--- Data loaded into Pandas DataFrame ---\n")
        stdscr.addstr("Enter query condition (e.g., name == 'Đinh Phương Sơn' or id == 2410874): ")
        
        curses.echo()
        query_str = stdscr.getstr().decode('utf-8')
        curses.noecho()
        
        if query_str:
            result = df_students.query(query_str)
            if not result.empty:
                stdscr.addstr(f"\nQuery Result:\n{result.to_string()}\n")
            else:
                stdscr.addstr("\nNo matching results found.\n")
        else:
            stdscr.addstr("\nNo condition entered.\n")
            
    except Exception as e:
        stdscr.addstr(f"\nQuery syntax error: {e}\n")
        
    stdscr.addstr("\nPress any key to return...")
    stdscr.getch()

def main(stdscr):
    students = []
    courses = []
    marks = {} 

    load_data(students, courses, marks)

    while True:
        stdscr.clear()
        stdscr.addstr("--- USTH Student Mark Management ---\n")
        stdscr.addstr("1. Input Students\n")
        stdscr.addstr("2. Input Courses\n")
        stdscr.addstr("3. Input Marks\n")
        stdscr.addstr("4. List Students (Sorted by GPA)\n")
        stdscr.addstr("5. Show Marks\n")
        stdscr.addstr("6. Save & Export CSV Data\n")
        stdscr.addstr("7. Pandas Query (Extra Task)\n")
        stdscr.addstr("8. Quit\n")
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
            save_and_export_data(students, courses, marks)
            stdscr.addstr("\nPickle saved and CSV exported successfully! Press any key...")
            stdscr.getch()
        elif choice == '7':
            pandas_query(stdscr)
        elif choice == '8':
            save_and_export_data(students, courses, marks)
            break

if __name__ == "__main__":
    curses.wrapper(main)
