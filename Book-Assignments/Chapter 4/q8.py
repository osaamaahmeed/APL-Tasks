import re

def extract_programming_lang(text):
    pattern = r"Python|Java|C\+\+|Ruby|Dart|Flutter|C\#|JavaScript"
    languages = re.findall(pattern, text)
    return languages

text = "I know Python, Java, anc C++ but not Ruby"
print(extract_programming_lang(text))