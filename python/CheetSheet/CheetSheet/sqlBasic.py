import sqlite3

# 1️⃣ Connect to database (creates 'school.db' if not exists)
conn = sqlite3.connect('school.db')
cur = conn.cursor()  # Cursor allows executing SQL commands

# 2️⃣ Create Tables
cur.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- unique ID
    name TEXT NOT NULL,                     -- student name, cannot be empty
    age INTEGER,                            -- age of student
    grade TEXT                              -- grade like A, B, C
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS teachers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    subject TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS subjects(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    teacher_id INTEGER,
    FOREIGN KEY(teacher_id) REFERENCES teachers(id)
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS scores(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject_id INTEGER,
    marks INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(id),
    FOREIGN KEY(subject_id) REFERENCES subjects(id)
)
""")

# 3️⃣ Insert Data
students_data = [('Parth', 20, 'A'), ('Alice', 19, 'B'), ('Bob', 21, 'C')]
for student in students_data:
    cur.execute("INSERT INTO students(name, age, grade) VALUES(?, ?, ?)", student)

teachers_data = [('Mr. Smith', 'Math'), ('Mrs. Lee', 'English')]
for teacher in teachers_data:
    cur.execute("INSERT INTO teachers(name, subject) VALUES(?, ?)", teacher)

subjects_data = [('Math', 1), ('English', 2)]
for subject in subjects_data:
    cur.execute("INSERT INTO subjects(name, teacher_id) VALUES(?, ?)", subject)

scores_data = [(1, 1, 95), (2, 2, 88), (3, 1, 76)]
for score in scores_data:
    cur.execute("INSERT INTO scores(student_id, subject_id, marks) VALUES(?, ?, ?)", score)

conn.commit()  # Save all changes

# 4️⃣ Select all students
print("All Students:")
cur.execute("SELECT * FROM students")
for row in cur.fetchall():
    print(row)

# 5️⃣ Students with marks > 80
print("\nStudents with marks > 80:")
cur.execute("""
SELECT students.name, scores.marks
FROM students
JOIN scores ON students.id = scores.student_id
WHERE scores.marks > 80
""")
for row in cur.fetchall():
    print(row)

# 6️⃣ Average marks per subject
print("\nAverage Marks per Subject:")
cur.execute("""
SELECT subjects.name, AVG(scores.marks) as avg_marks
FROM scores
JOIN subjects ON scores.subject_id = subjects.id
GROUP BY subjects.name
""")
for row in cur.fetchall():
    print(row)

# 7️⃣ Update marks (e.g., Bob gets 100 in Math)
cur.execute("UPDATE scores SET marks = 100 WHERE student_id = 3 AND subject_id = 1")
conn.commit()

# 8️⃣ Delete a student (e.g., Alice)
cur.execute("DELETE FROM students WHERE name='Alice'")
conn.commit()

# 9️⃣ Join tables to see all scores with names
print("\nAll Scores:")
cur.execute("""
SELECT students.name, subjects.name, scores.marks
FROM scores
JOIN students ON scores.student_id = students.id
JOIN subjects ON scores.subject_id = subjects.id
""")
for row in cur.fetchall():
    print(row)

# 1️⃣0️⃣ Order students by marks descending
print("\nStudents ordered by marks:")
cur.execute("""
SELECT students.name, scores.marks
FROM students
JOIN scores ON students.id = scores.student_id
ORDER BY scores.marks DESC
""")
for row in cur.fetchall():
    print(row)

# Close connection
conn.close()
