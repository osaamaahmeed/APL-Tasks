import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan'],
    'Age': [20, 21, 19, 22, 20],
    'Score': [75, 82, 95, 68, 88] 
}

df = pd.DataFrame(data)

high_scorers = df[df['Score'] > 80]

print("Students with Score > 80:")
print(high_scorers)