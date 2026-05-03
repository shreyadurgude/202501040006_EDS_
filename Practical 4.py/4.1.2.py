import pandas as pd  # Import pandas library and use alias 'pd'
# Provided dictionary of lists
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],  # List containing names
    'Age': [25, 30, 35],                 # List containing ages
}
# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)  
# Converts dictionary into a table (DataFrame)
# Display the original DataFrame
print("Original DataFrame:")  
# Print heading
print(df)  
# Show the initial dataset
# Adding a new row
new_name = input("New name: ")   # Take new name from user
new_age = int(input("New age: "))   # Take new age and convert to integer
df.loc[len(df)] = [new_name, new_age]  # Add new row at the end of DataFrame
# len(df) gives next index position
# Display the DataFrame after adding a new row
print("After adding a row:\n", df)   # Show updated DataFrame
# Modifying a row
row_to_modify = int(input("Index of row to modify: "))   # Take index of row to modify
new_age_value = int(input("New age: "))   # Take new age value
df.at[row_to_modify, "Age"] = new_age_value   # Update specific cell (row, column)

# Display the DataFrame after modifying a row
print("After modifying a row:")  
print(df)


# Deleting a row
row_to_delete = int(input("Index of row to delete: "))   # Take index to delete

df = df.drop(index=row_to_delete).reset_index(drop=True)  
# drop() removes row
# reset_index() reorders index after deletion
# Display the DataFrame after deleting a row
print("After deleting a row:")  
print(df)


# Adding a new column
genders = input("Enter genders separated by space: ").split()    # Take multiple gender values and convert to list

df["Gender"] = genders  
# Add new column 'Gender'

# Display the DataFrame after adding the new column
print("After adding a new column:")  
print(df)

# Modifying a column
df["Name"] = df["Name"].str.upper()   # Convert all names to uppercase

# Display the DataFrame after modifying the column
print("After modifying a column:")  
print(df)


# Deleting a column
df = df.drop(columns=["Age"])   # Remove 'Age' column

# Display the DataFrame after deleting the column
print("After deleting a column:")  
print(df)
