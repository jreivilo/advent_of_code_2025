with open('input.txt', 'r') as f:
	lines = f.readlines()

# Last line contains operators
operator_line = lines[-1].strip()
# First lines contain numbers arranged in columns
number_lines = [line.rstrip('\n') for line in lines[:-1]]

# In cephalopod math, we need to read right-to-left by character position
# Each character position forms a digit, reading top to bottom forms a number

# Find the maximum line length to know how wide the worksheet is
max_len = max(len(line) for line in number_lines)

# Pad all lines to the same length
padded_lines = [line.ljust(max_len) for line in number_lines] # add spaces to the right as needed

# Read right-to-left, column by column
problems = []
operators = []
current_problem = []

for col_idx in range(max_len - 1, -1, -1):  # Right to left
	# Get all characters in this column
	column_chars = [line[col_idx] for line in padded_lines]
	
	# Get the operator character at this position
	if col_idx < len(operator_line):
		op_char = operator_line[col_idx]
	else:
		op_char = ' '
	
	# Check if this column is all spaces (separator between problems)
	if all(c == ' ' for c in column_chars) and op_char == ' ':
		# This is a separator - save the current problem if it exists
		if current_problem:
			problems.append(current_problem)
			current_problem = []
	else:
		# This column contains digits - form a number from top to bottom
		digits = [c for c in column_chars if c != ' ']
		if digits:
			number = int(''.join(digits))
			current_problem.append(number)
		
		# Save the operator for this problem
		if op_char in ['*', '+']:
			operators.append(op_char)

# Don't forget the last problem
if current_problem:
	problems.append(current_problem)

# Reverse problems and operators since we built them right-to-left
problems.reverse()
operators.reverse()

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

