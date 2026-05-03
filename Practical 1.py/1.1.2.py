n=int(input())
digits = len(str(n))
if digits == 1:
	print(n*n)
elif digits == 2:
	print(f"{n**0.5:.2f}")
elif digits == 3:
	print(f"{n**(1/3):.2f}")
else:
	print("Invalid")
