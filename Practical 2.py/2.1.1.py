# Initialize empty list
numbers = []

while True:
	# Display menu
	print("1. Add")
	print("2. Remove")
	print("3. Display")
	print("4. Quit")

	choice = input("Enter choice: ")

	# Add
	if choice == '1':
		val = input("Integer: ")
		try:
			num = int(val)
			numbers.append(num)
			print(f"List after adding: {numbers}")
		except:
			print("Invalid input")

	# Remove
	elif choice == '2':
		if not numbers:
			print("List is empty")
		else:
			val = input("Integer: ")
			try:
				num = int(val)
				if num in numbers:
					numbers.remove(num)
					print(f"List after removing: {numbers}")
				else:
					print("Element not found")
			except:
				print("Invalid input")

	# Display
	elif choice == '3':
		if not numbers:
			print("List is empty")
		else:
			print(numbers)

	# Quit
	elif choice == '4':
		break

	# Invalid choice
	else:
		print("Invalid choice")
