import re

def count_freq(text):
    words = re.findall(r"\w+", text)
    freq_map = {}
    for word in words:
        if word in freq_map:
            freq_map[word]+=1
        else:
            freq_map[word] = 1
    return freq_map

text = "Python, Python! AI is great; Python AI."
print(count_freq(text))