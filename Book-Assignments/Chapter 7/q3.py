import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), 'school.db')

conn = sqlite3.connect(db_path)
cursor = conn.cursor()


# --- THE TRANSACTION CHALLENGE ---
print("\n--- Starting Transaction ---")

try:
    cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ('NewStudent1', 88.0))
    cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ('NewStudent2', 91.5))

    error_trigger = 1 / 0  

    conn.commit()
    print("Transaction Committed.")

except ZeroDivisionError as e:
    print(f"Error occurred: {e}")
    conn.rollback() 
    print("Transaction rolled back.")


print("\n--- Final Records ---")

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)


conn.close()