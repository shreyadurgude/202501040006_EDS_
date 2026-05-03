# Initial dictionary with 10 predefined records
student = {
    1: "Amit",
    2: "Riya",
    3: "Kiran",
    4: "Neha",
    5: "Arjun",
    6: "Pooja",
    7: "Rahul",
    8: "Sneha",
    9: "Vikram",
    10: "Anjali"
}

# Display original dictionary
print(f"Original Dictionary: {student}")

# Insertion
key = int(input())
value = input()
student[key] = value
print(f"After Insertion: {student}")

# Update - only if the key exists
key = int(input())
value = input()
if key in student:
	student[key] = value
print(f"After Update: {student}")

# Deletion - only if the key exists
key = int(input())
if key in student:
	del student[key]
print(f"After Deletion: {student}")

# Traversing
print("Traversing Dictionary:")
for k, v in student.items():
	print(f"{k} : {v}")
