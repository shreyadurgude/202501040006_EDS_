# Type Content here...
# Input: number of rows
n = int(input())

# Outer loop for rows
for i in range(1, n + 1):
	# Inner loop for numbers in each row
	for j in range(1, i + 1):
		print(j, end=" ")
	print()  # Move to next line
