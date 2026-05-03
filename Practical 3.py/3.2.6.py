import numpy as np

# Input array from the user
array1 = np.array(list(map(int, input().split())))

# Searching
search_value = int(input("Value to search: "))
count_value = int(input("Value to count: "))
broadcast_value = int(input("Value to add: "))

# 1. Find indices where search_value matches in array1
# np.where returns a tuple, so we extract the first element
indices = np.where(array1 == search_value)[0]
print(indices)

# 2. Count occurrences in array1
count = np.count_nonzero(array1 == count_value)
print(count)

# 3. Broadcasting addition
# Adding a scalar to a NumPy array automatically uses broadcasting
broadcasted_array = array1 + broadcast_value
print(broadcasted_array)

# 4. Sort the first array
# np.sort returns a sorted copy of the array in ascending order
sorted_array = np.sort(array1)
print(sorted_array)
