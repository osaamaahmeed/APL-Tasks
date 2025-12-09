data = [10, 20, 30, 40, 50]

# To Normalize list of numbers we use this formula: (x - min) / (max - min)

min_val = min(data)
max_val = max(data)

normalized_data = list(map(lambda x: (x - min_val) / (max_val - min_val), data))

print("Normalized Data:", normalized_data)