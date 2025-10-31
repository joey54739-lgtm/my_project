import sqlite3

# Connect to database
conn = sqlite3.connect('school.db')
cur = conn.cursor()

# Function to create tables
def create_tables():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        grade TEXT
    )""")
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS teachers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        subject TEXT
    )""")
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS subjects(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        teacher_id INTEGER,
        FOREIGN KEY(teacher_id) REFERENCES teachers(id)
    )""")
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS scores(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        subject_id INTEGER,
        marks INTEGER,
        FOREIGN KEY(student_id) REFERENCES students(id),
        FOREIGN KEY(subject_id) REFERENCES subjects(id)
    )""")
    
    conn.commit()
    print("Tables created successfully!")

# Function to insert data
def insert_data():
    print("\n1. Insert Student\n2. Insert Teacher\n3. Insert Subject\n4. Insert Score")
    choice = input("Enter choice: ")
    
    if choice == "1":
        name = input("Student Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        cur.execute("INSERT INTO students(name, age, grade) VALUES(?, ?, ?)", (name, age, grade))
    
    elif choice == "2":
        name = input("Teacher Name: ")
        subject = input("Subject: ")
        cur.execute("INSERT INTO teachers(name, subject) VALUES(?, ?)", (name, subject))
    
    elif choice == "3":
        name = input("Subject Name: ")
        teacher_id = int(input("Teacher ID: "))
        cur.execute("INSERT INTO subjects(name, teacher_id) VALUES(?, ?)", (name, teacher_id))
    
    elif choice == "4":
        student_id = int(input("Student ID: "))
        subject_id = int(input("Subject ID: "))
        marks = int(input("Marks: "))
        cur.execute("INSERT INTO scores(student_id, subject_id, marks) VALUES(?, ?, ?)", (student_id, subject_id, marks))
    
    else:
        print("Invalid choice!")
        return
    
    conn.commit()
    print("Data inserted successfully!")

# Function to select data
def select_data():
    print("\n1. Show All Students\n2. Show All Teachers\n3. Show All Subjects\n4. Show All Scores\n5. Filter Students by Marks > X")
    choice = input("Enter choice: ")
    
    if choice == "1":
        cur.execute("SELECT * FROM students")
    elif choice == "2":
        cur.execute("SELECT * FROM teachers")
    elif choice == "3":
        cur.execute("SELECT * FROM subjects")
    elif choice == "4":
        cur.execute("""
        SELECT students.name, subjects.name, scores.marks
        FROM scores
        JOIN students ON scores.student_id = students.id
        JOIN subjects ON scores.subject_id = subjects.id
        """)
    elif choice == "5":
        x = int(input("Enter minimum marks: "))
        cur.execute("""
        SELECT students.name, scores.marks
        FROM students
        JOIN scores ON students.id = scores.student_id
        WHERE scores.marks > ?
        """, (x,))
    else:
        print("Invalid choice!")
        return
    
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Function to update data
def update_data():
    print("\nUpdate student marks")
    student_id = int(input("Student ID: "))
    subject_id = int(input("Subject ID: "))
    marks = int(input("New Marks: "))
    cur.execute("UPDATE scores SET marks = ? WHERE student_id = ? AND subject_id = ?", (marks, student_id, subject_id))
    conn.commit()
    print("Marks updated successfully!")

# Function to delete data
def delete_data():
    print("\n1. Delete Student\n2. Delete Teacher\n3. Delete Subject\n4. Delete Score")
    choice = input("Enter choice: ")
    
    if choice == "1":
        student_id = int(input("Student ID to delete: "))
        cur.execute("DELETE FROM students WHERE id = ?", (student_id,))
    elif choice == "2":
        teacher_id = int(input("Teacher ID to delete: "))
        cur.execute("DELETE FROM teachers WHERE id = ?", (teacher_id,))
    elif choice == "3":
        subject_id = int(input("Subject ID to delete: "))
        cur.execute("DELETE FROM subjects WHERE id = ?", (subject_id,))
    elif choice == "4":
        score_id = int(input("Score ID to delete: "))
        cur.execute("DELETE FROM scores WHERE id = ?", (score_id,))
    else:
        print("Invalid choice!")
        return
    
    conn.commit()
    print("Data deleted successfully!")

# Main interactive loop
while True:
    print("\n===== SQLite3 School Database Menu =====")
    print("1. Create Tables")
    print("2. Insert Data")
    print("3. Select Data")
    print("4. Update Data")
    print("5. Delete Data")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        create_tables()
    elif choice == "2":
        insert_data()
    elif choice == "3":
        select_data()
    elif choice == "4":
        update_data()
    elif choice == "5":
        delete_data()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")

# Close connection
conn.close()
