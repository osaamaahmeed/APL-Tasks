import numpy as np

numbers = np.arange(1, 11)

mean_val = np.mean(numbers)
median_val = np.median(numbers)
std_dev = np.std(numbers)


print(f"Mean: {mean_val}")
print(f"Median: {median_val}")
print(f"Standard Deviation: {std_dev:.3f}")
