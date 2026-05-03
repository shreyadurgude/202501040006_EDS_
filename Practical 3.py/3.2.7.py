import numpy as np

a = np.loadtxt("Sample.csv", delimiter=',', skiprows=1)

# 1. Print all student details
print("All student Details:\n", a)

# 2. print total students
print("Total Students:", a.shape[0])

# 3. Print all student Roll numbers
print("All Student Roll Nos", a[:, 0])

# 4. Print subject 1 marks
print("Subject 1 Marks", a[:, 1])

# 5. print minimum marks of Subject 2
print("Min marks in Subject 2", np.min(a[:, 2]))

# 6. print maximum marks of Subject 3
print("Max marks in Subject 3", np.max(a[:, 3]))

# 7. Print All subject marks
print("All subject marks:", a[:, 1:4])

# 8. print Total marks of students
total_marks = np.sum(a[:, 1:4], axis=1)
print("Total Marks", total_marks)

# 9. print average marks of each student
avg_student = np.round(np.mean(a[:, 1:4], axis=1), 1)
print(avg_student)

# 10. print average marks of each subject
avg_subject = np.round(np.mean(a[:, 1:4], axis=0), 1)
print("Average Marks of each subject", avg_subject)

# 11. print average marks of S1 and S2
print("Average Marks of S1 and S2", avg_subject[0:2])

# 12. print average marks of S1 and S3
print("Average Marks of S1 and S3", avg_subject[[0, 2]])

# 13. print Roll number who got maximum marks in Subject 3
print("Roll no who got maximum marks in Subject 3", a[np.argmax(a[:, 3]), 0])

# 14. print Roll number who got minimum marks in Subject 2
print("Roll no who got minimum marks in Subject 2", a[np.argmin(a[:, 2]), 0])

# 15. print Roll number who got 24 marks in Subject 2
print("Roll no who got 24 marks in Subject 2", a[a[:, 2] == 24][:, [0]])

# 16. print count of students who got marks in Subject 1 < 40
print("Count of students who got marks in Subject 1 < 40", np.sum(a[:, 1] < 40))

# 17. print count of students who got marks in Subject 2 > 90
print("Count of students who got marks in Subject 2 > 90:", np.sum(a[:, 2] > 90))

# 18. print count of students in each subject who got marks >= 90
print("Count of students in each subject who got marks >= 90:", np.sum(a[:, 1:4] >= 90, axis=0))

# 19. print count of subjects in which each student got marks >= 90
print("Roll no:", a[:, 0])
print("Count of subjects in which student got marks >= 90:", np.sum(a[:, 1:4] >= 90, axis=1))

# 20. Print S1 marks in ascending order
print(np.sort(a[:, 1]))

# 21. Print students who scored between 50 and 90 in Subject 1
print(a[(a[:, 1] >= 50) & (a[:, 1] <= 90)])

# 22. Print ALL student details again (this was missing ❗)
print(a)

# 23. Print index positions of students who scored 79 in Subject 1
print(np.where(a[:, 1] == 79))
