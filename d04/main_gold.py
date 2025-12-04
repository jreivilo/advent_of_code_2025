import numpy as np

with open('input.txt', 'r') as f:
	lines = f.readlines()

total_nb_taken = 0

# Represent this as a matrix of integers where @ is 1 and . is 0
matrix = []
for line in lines:
	# Remove trailing newline and skip empty lines
	trimmed = line.rstrip('\n')
	if not trimmed:
		continue
	
	row = [1 if char == '@' else 0 for char in trimmed]
	matrix.append(row)


def count_and_remove_neighbors(matrix) :
	nb_roll_taken = 0
	rows = len(matrix)
	cols = len(matrix[0]) if rows > 0 else 0

	matrix_without_roll_taken = [row[:] for row in matrix]  # Deep copy of the matrix

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
					nb_roll_taken += 1
					# Remove the roll
					matrix_without_roll_taken[r][c] = 0

	return nb_roll_taken, matrix_without_roll_taken

nb_roll_taken = 1  # Initialize to enter the loop
while nb_roll_taken > 0:
	nb_roll_taken, matrix = count_and_remove_neighbors(matrix)
	total_nb_taken += nb_roll_taken

print("Total roll-accessible positions:", total_nb_taken)