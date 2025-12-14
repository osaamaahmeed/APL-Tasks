import json
import os


file_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(file_dir, "course.json")
with open(file_path, "r") as json_file:
    loaded_data = json.load(json_file)

print(loaded_data['students'])