sentences = ["Hello world", "Python is fun", "Map and Lambda"]

word_lengths = list( map( lambda s: list( map( len, s.split() ) ), sentences ) )

print("Word Lengths:", word_lengths)