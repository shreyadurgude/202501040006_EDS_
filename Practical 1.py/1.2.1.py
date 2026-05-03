# Input: number of courses
n = int(input())

# Input: marks of the courses
marks = list(map(int, input().split()))

# Check if student failed in any course
for m in marks:
	if m < 40:
		print("Fail")
		break
else:
	# Calculate aggregate percentage
	percentage = sum(marks) / n

	# Print percentage with 2 decimal places
	print(f"Aggregate Percentage: {percentage:.2f}")

	# Determine grade
	if percentage > 75:
		print("Grade: Distinction")
	elif percentage >= 60:
		print("Grade: First Division")
	elif percentage >= 50:
		print("Grade: Second Division")
	elif percentage >= 40:
		print("Grade: Third Division")
