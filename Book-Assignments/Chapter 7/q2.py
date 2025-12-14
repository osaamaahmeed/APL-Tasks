import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), 'school.db')

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("\n--- Add New Student ---")


new_name = input("Enter name: ")
new_grade = float(input("Enter grade: "))

cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", (new_name, new_grade))
conn.commit()

print("\n--- Updated Records ---")
cursor.execute("SELECT * FROM students")
updated_rows = cursor.fetchall()
for row in updated_rows:
    print(row)

