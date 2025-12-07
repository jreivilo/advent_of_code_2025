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
		print("Found 'S' row")
		start_x = row.index('S')
		# Replace 'S' with '|' on the second row, same column
		print(f"Placing '|' at ({start_x}, {y + 1})")
		grid[y + 1][start_x] = '|'
		continue

	# Check all positions for '|' in this row
	for x, char in enumerate(row):
		if char == '|':
			print(f"Found '|' at ({x}, {y})")
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

print(f"Total splits added: {split_count}")
# print("Final grid:")
# for row in grid:
# 	print(''.join(row))