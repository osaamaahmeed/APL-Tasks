def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result = result + char
    return result

print(remove_vowels("Hello World"))