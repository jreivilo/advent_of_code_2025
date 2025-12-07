with open('input.txt', 'r') as f:
	lines = f.readlines()

# Last line contains operators
operators = lines[-1].strip().split()
# First lines contain numbers arranged in columns
number_lines = [line.rstrip('\n') for line in lines[:-1]]

print("Operators:", operators)
# Parse numbers into a 2D grid where each row is from the file
# We need to split by spaces and handle variable spacing
grid = []
for line in number_lines:
	row = line.split()
	grid.append(row)

# Transpose to get columns (each column is a problem)
num_columns = max(len(row) for row in grid)
problems = []

for col_idx in range(num_columns):
	problem_numbers = []
	for row in grid:
		if col_idx < len(row):
			problem_numbers.append(int(row[col_idx]))
	problems.append(problem_numbers)


# Calculate result for each problem
grand_total = 0

for i, (numbers, op) in enumerate(zip(problems, operators)):
	if op == '*':
		result = 1
		for num in numbers:
			result *= num
	elif op == '+':
		result = sum(numbers)
	else:
		raise ValueError(f"Unknown operator: {op}")
	
	print(f"Problem {i+1}: {' '.join(map(str, numbers))} {op} = {result}")
	grand_total += result

print(f"\nGrand Total: {grand_total}")

