import re
def extract_hashtags(text):
    pattern = r"#\w+"
    hashtags = re.findall(pattern, text)
    print(hashtags)


text = "I love #Python and #AI"
extract_hashtags(text)