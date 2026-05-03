import pandas as pd

# Read the text file into a DataFrame
file = input()
data = pd.read_csv(file, sep="\s+", header=None, names=["Name", "Age", "Grade"])
# 1. Display the first five rows
print("First five rows:")
print(data.head())

# 2. Calculate the average age (rounded to 2 decimal places)
avg_age = round(data["Age"].mean(), 2)
print(f"Average age: {avg_age}")

# 3. Filter students with grade up to 'B' (A and B only)
filtered_data = data[data["Grade"].isin(["A", "B"])]

print("Students with a grade up to B")
print(filtered_data)
