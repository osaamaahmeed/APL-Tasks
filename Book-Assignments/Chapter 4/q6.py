import re

def extract_dates(text):
    pattern = r"\d{4}-\d{2}-\d{2}"
    dates = re.findall(pattern, text)
    return dates

text = "The events are on 2023-05-12 and 2024-01-01"
print(extract_dates(text))