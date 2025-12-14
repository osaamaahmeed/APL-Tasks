import csv
import json
import os

def convert_csv_to_json(csv_filename, json_filename):
    people_list = []

    file_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(file_dir, csv_filename)
    with open(file_path, mode='r', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            row["Age"] = int(row["Age"])
            people_list.append(row)
    
    final_structure = {
        "people": people_list
    }
    
    json_path = os.path.join(file_dir, json_filename)
    with open(json_path, 'w') as json_file:
        json.dump(final_structure, json_file, indent=4)
        
    print(f"Successfully converted '{csv_filename}' to '{json_filename}'")

convert_csv_to_json("source.csv", "output.json")