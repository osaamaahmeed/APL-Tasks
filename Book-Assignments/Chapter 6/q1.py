import csv
import os

def process_grades(fileName):
    file_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(file_dir, fileName)
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        print("Students with grades above 80:")
        print("==============================")
        for row in reader:
            grade = int(row['Grade'])
            if (grade > 80):
                name = row['Name']
                print(f"{name} with Grade: {grade}")

process_grades('students.csv')