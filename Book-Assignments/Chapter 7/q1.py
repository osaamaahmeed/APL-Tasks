import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), 'school.db')

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# to drop table if exists so we start fresh every time we run the code
cursor.execute("DROP TABLE IF EXISTS students")

cursor.execute('''
    CREATE TABLE students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        grade REAL
    )
''')

initial_students = [
    ('Ali', 85.5),
    ('Sara', 92.0),
    ('Mohamed', 78.3)
]
    
cursor.executemany("INSERT INTO students (name, grade) VALUES (?, ?)", initial_students)
conn.commit()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
