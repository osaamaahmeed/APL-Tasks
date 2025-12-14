import pandas as pd
import os

file_dir = os.path.dirname(os.path.abspath(__file__))
excel_path = os.path.join(file_dir, "employees.xlsx")

data = {
    "ID": [101, 102, 103],
    "Name": ["John", "Emily", "Michael"],
    "Salary": [50000, 60000, 55000]
}
df = pd.DataFrame(data)

df.to_excel(excel_path, index=False)

df_read = pd.read_excel(excel_path)

print(df_read[["Name", "Salary"]])