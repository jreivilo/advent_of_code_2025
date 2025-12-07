with open('input.txt', 'r') as f:
	lines = f.readlines()

grid = []
for line in lines:
	row = list(line.rstrip('\n'))
	grid.append(row)

split_count = 0

for y, row in enumerate(grid):
	# Find the 'S' on the first row
	if 'S' in row:
		start_x = row.index('S')
		# Replace 'S' with '|' on the second row, same column
		grid[y + 1][start_x] = '|'
		continue

	# Check all positions for '|' in this row
	for x, char in enumerate(row):
		if char == '|':
			if y + 1 < len(grid):
				if '^' in grid[y + 1][x]:
					# Add '|' on the right and left of '^'
					split_count += 1
					if x > 0:
						grid[y + 1][x - 1] = '|'
					if x < len(grid[y + 1]) - 1:
						grid[y + 1][x + 1] = '|'
				else:
					# No '^' on next row, just add '|' directly below
					grid[y + 1][x] = '|'


from functools import lru_cache

# Convert grid to tuple for hashing (needed for lru_cache)
grid_tuple = tuple(tuple(row) for row in grid)

@lru_cache(maxsize=None)
def count_unique_paths(y, x):
	"""Count unique paths from (y, x) to the bottom of the grid."""
	if y >= len(grid_tuple):
		return 1  # Reached the bottom
	
	# Check if current position is valid
	if x < 0 or x >= len(grid_tuple[y]) or grid_tuple[y][x] not in ['|', 'S']:
		return 0  # Not a valid path
	
	total_paths = 0
	if y + 1 < len(grid_tuple):
		if '^' in grid_tuple[y + 1][x]:
			# Split paths to left and right of '^'
			if x > 0:
				total_paths += count_unique_paths(y + 1, x - 1)
			if x < len(grid_tuple[y + 1]) - 1:
				total_paths += count_unique_paths(y + 1, x + 1)
		else:
			# Continue straight down
			total_paths += count_unique_paths(y + 1, x)
	else:
		# Reached bottom
		return 1
	
	return total_paths

print(f"Total splits added: {split_count}")
total_unique_paths = count_unique_paths(0, start_x)
print(f"Total unique paths from 'S' to bottom: {total_unique_paths}")
print(f"Cache info: {count_unique_paths.cache_info()}")