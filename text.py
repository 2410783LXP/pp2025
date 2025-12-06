class Student:
    def __init__(self, sid, name, dob):
        self.sid = sid
        self.name = name
        self.dob = dob
        self.marks = {}

    def set_mark(self, course_id, mark):
        self.marks[course_id] = mark


class Course:
    def __init__(self, cid, name):
        self.cid = cid
        self.name = name


class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        n = int(input("Number of students: "))
        for _ in range(n):
            sid = input("Student ID: ")
            name = input("Student name: ")
            dob = input("Student DoB: ")
            self.students.append(Student(sid, name, dob))

    def input_courses(self):
        n = int(input("Number of courses: "))
        for _ in range(n):
            cid = input("Course ID: ")
            name = input("Course name: ")
            self.courses.append(Course(cid, name))

    def input_marks(self):
        cid = input("Enter course ID to input marks: ")
        found = False

        for c in self.courses:
            if c.cid == cid:
                found = True
                print(f"Entering marks for course: {c.name}")
                break

        if not found:
            print("Course not found!")
            return

        for s in self.students:
            mark = float(input(f"Enter mark for {s.name}: "))
            s.set_mark(cid, mark)

    def list_students(self):
        print("\n=== Students ===")
        for s in self.students:
            print(f"- ID: {s.sid}, Name: {s.name}, DoB: {s.dob}")

    def list_courses(self):
        print("\n=== Courses ===")
        for c in self.courses:
            print(f"- ID: {c.cid}, Name: {c.name}")

    def show_marks(self):
        cid = input("Enter course ID: ")
        print(f"\nMarks for course {cid}:")
        for s in self.students:
            if cid in s.marks:
                print(f"- {s.name}: {s.marks[cid]}")
            else:
                print(f"- {s.name}: No mark")

school = School()
while True:
    print("""\nStudent Mark Management System
    1. Input students
    2. Input courses
    3. Input marks for a course
    4. List students
    5. List courses
    6. Show marks for a course
    0. Exit""")

    choice = input("Choose an option: ")

    if choice == '1':
        school.input_students()
    elif choice == '2':
        school.input_courses()
    elif choice == '3':
        school.input_marks()
    elif choice == '4':
        school.list_students()
    elif choice == '5':
        school.list_courses()
    elif choice == '6':
        school.show_marks()
    elif choice == '0':
        break
    else:
        print("Invalid choice!")
