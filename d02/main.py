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
	if len(str_id) % 2 == 0:
		half_length = len(str_id) // 2
		first_half = str_id[:half_length]
		second_half = str_id[half_length:]
		if first_half == second_half:
			invalid_id.append(id)
			print(f"Invalid ID found: {id}")

# Calculate the sum of invalid IDs
sum_invalid_ids = sum(invalid_id)
print(f"Sum of invalid IDs: {sum_invalid_ids}")