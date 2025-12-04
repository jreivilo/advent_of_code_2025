import numpy as np

total_roll_accessible = 0

with open('input.txt', 'r') as f:
	lines = f.readlines()

# Represent this as a matrix of integers where @ is 1 and . is 0
matrix = []
for line in lines:
	# Remove trailing newline and skip empty lines
	trimmed = line.rstrip('\n')
	if not trimmed:
		continue
	
	row = [1 if char == '@' else 0 for char in trimmed]
	matrix.append(row)

# For each cell that is 1, check its 8 neighbors
rows = len(matrix)
cols = len(matrix[0]) if rows > 0 else 0

# Fi there are 4 or fewer neighboring 1s, increment the total count
for r in range(rows):
	for c in range(cols):
		if matrix[r][c] == 1:
			# Check neighbors
			neighbor_coords = [
				(r-1, c-1), (r-1, c), (r-1, c+1),
				(r, c-1),           (r, c+1),
				(r+1, c-1), (r+1, c), (r+1, c+1)
			]
			neighbor_count = 0
			for nr, nc in neighbor_coords:
				if 0 <= nr < rows and 0 <= nc < cols:
					if matrix[nr][nc] == 1:
						neighbor_count += 1
			if neighbor_count < 4:
				total_roll_accessible += 1

print("Total roll-accessible positions:", total_roll_accessible)