heights = list(map(int,input().split()))

tallest = heights[0]
for h in heights:
	if h > tallest:
		tallest = h
print(tallest)
