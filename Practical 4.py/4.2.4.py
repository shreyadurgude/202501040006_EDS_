import pandas as pd
from itertools import combinations
from collections import Counter

# Prompt user to input the file name
file_name = input()

# Read data from the specified CSV file
df = pd.read_csv(file_name)

# Step 1: Group products by date
grouped = df.groupby('Date')['Product'].apply(list)

# Step 2: Generate pairs and count frequency
pair_counter = Counter()

for products in grouped:
    # Get unique products per date (avoid duplicates if any)
    unique_products = list(set(products))
    
    # Generate all pairs
    pairs = combinations(sorted(unique_products), 2)
    
    pair_counter.update(pairs)

# Step 3: Find maximum frequency
max_count = max(pair_counter.values())

# Step 4: Print pairs with maximum frequency
for pair, count in pair_counter.items():
    if count == max_count:
        print(f"{pair[0]} and {pair[1]}: {count} times")
