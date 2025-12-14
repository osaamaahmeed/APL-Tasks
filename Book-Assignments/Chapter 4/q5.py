import re

def find_duplicate(text):
    pattern = r"\b(\w+)\s+\1\b"
    matches = [match.group() for match in re.finditer(pattern, text)]
    return matches

text = "This is is a test test"
print(find_duplicate(text))