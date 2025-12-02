invalid_id = []
all_possible_ids = []

with open('input.txt', 'r') as f:
	lines = f.readlines()
	# Each line contains two ranges in the format "a-b,c-d"
	range_pairs = lines[0].strip().split(',')

# Extract lower and upper bounds for each range
for pair in range_pairs:
	lower_bound = int(pair.split('-')[0])
	upper_bound = int(pair.split('-')[1])

	all_possible_ids += list(range(lower_bound, upper_bound + 1))


# Identify invalid IDs
for id in all_possible_ids:

	# Invalid if it has pairs number of digits, then split in half are the same like 1010 (10 and 10
	str_id = str(id)
	max_modulo = len(str_id)
	for modulo in range(2, max_modulo + 1, 1):
		if len(str_id) % modulo == 0:
			split_length = len(str_id) // modulo
			parts = [str_id[i*split_length:(i+1)*split_length] for i in range(modulo)]
			# If all parts are the same, then invalid
			if all(part == parts[0] for part in parts):
				invalid_id.append(id)
				print(f"Invalid ID found: {id}")
				break

# Calculate the sum of invalid IDs
sum_invalid_ids = sum(invalid_id)
print(f"Sum of invalid IDs: {sum_invalid_ids}")