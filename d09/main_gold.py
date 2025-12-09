from tqdm import tqdm

with open('input.txt') as f:
	lines = f.read().strip().split('\n')

def display_grid(red_set, green_set, orange_set=None):
	# Determine grid bounds
	min_x = min(x for x, y in red_set.union(green_set))
	max_x = max(x for x, y in red_set.union(green_set))
	min_y = min(y for x, y in red_set.union(green_set))
	max_y = max(y for x, y in red_set.union(green_set))
	
	for y in range(min_y, max_y + 1):
		row = ''
		for x in range(min_x, max_x + 1):
			if (x, y) in red_set:
				row += 'R'
			elif (x, y) in green_set:
				row += 'G'
			elif orange_set and (x, y) in orange_set:
				row += 'I'
			else:
				row += '.'
		print(row)

# Parse coordinates
coordinates = []
for line in lines:
	x, y = map(int, line.split(','))
	coordinates.append((x, y))

# Build sets for red and green tiles
red_set = set(coordinates)
green_set = set()

print("\nBuilding green boundary tiles...")
# Build green tiles (connecting consecutive red tiles)
for i in tqdm(range(len(coordinates)), desc="Building boundaries"):
	x1, y1 = coordinates[i]
	x2, y2 = coordinates[(i + 1) % len(coordinates)]
	
	if x1 == x2:  # Same column
		for y in range(min(y1, y2), max(y1, y2) + 1):
			if (x1, y) not in red_set:
				green_set.add((x1, y))
	elif y1 == y2:  # Same row
		for x in range(min(x1, x2), max(x1, x2) + 1):
			if (x, y1) not in red_set:
				green_set.add((x, y1))

# Find largest rectangle area
max_area = 0

# Cache the union of all points to check (computed once)
all_points = red_set.union(green_set)

# Sort coordinate pairs by potential area (descending) to find large rectangles early
coord_pairs = []
for i in range(len(coordinates)):
	for j in range(i + 1, len(coordinates)):
		x1, y1 = coordinates[i]
		x2, y2 = coordinates[j]
		area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
		coord_pairs.append((area, i, j))

coord_pairs.sort(reverse=True, key=lambda x: x[0])

with tqdm(total=len(coord_pairs), desc="Finding rectangles") as pbar:
	for area, i, j in coord_pairs:
		# Skip if this area can't beat the current max
		if area <= max_area:
			pbar.update(1)
			continue
		
		x1, y1 = coordinates[i]
		x2, y2 = coordinates[j]
		
		# Define rectangle boundaries #NOT CORRECT FOR x1-x2 <=1 OR y1-y2 <=1
		min_x = min(x1, x2) + 1
		max_x = max(x1, x2) - 1
		min_y = min(y1, y2) + 1
		max_y = max(y1, y2) - 1
		
		# Check if any point is inside this rectangle using generator expression
		has_internal_point = any(min_x <= x <= max_x and min_y <= y <= max_y 
		                         for x, y in all_points)
		
		# Only consider rectangles without internal points
		if not has_internal_point:
			print(f"New max area {area} with corners ({x1},{y1}) and ({x2},{y2})")
			max_area = area
		
		pbar.update(1)

# display_grid(red_set, green_set)
	