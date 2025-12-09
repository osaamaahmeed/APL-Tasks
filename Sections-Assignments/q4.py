words = ["python", "lambda", "programming", "map", "function"]

first_last = list(map(lambda w: (w[0], w[-1]), words))
# first_last = list(map(lambda w: (w[0], w[len(w)-1]), words))

print("First & Last Characters:", first_last)