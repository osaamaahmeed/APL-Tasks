def etl_pipeline(strings_list):
    stop_words = {"the", "a", "is", "in", "of"}
    tokenized_words = []

    for text in strings_list:
        words = text.split()
        for word in words:
            tokenized_words.append(word.lower())
    
    filterd_words = []
    for word in tokenized_words:
        if word not in stop_words:
            filterd_words.append(word)
    
    words_freq = {}
    for word in filterd_words:
        if word in words_freq:
            words_freq[word] = words_freq[word]+1
        else:
            words_freq[word] = 1
    
    return words_freq

sentences = ["The cat is in the hat", "A cat is a nice pet", "I used to have a cat", "I don't have a cat right now"]
output = etl_pipeline(sentences)

for word, freq in output.items():
    print(word, freq)