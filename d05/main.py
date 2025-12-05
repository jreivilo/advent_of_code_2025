def parse_input(filename: str) -> tuple[list[str], list[int]]:
	"""Split input file into ranges and individual IDs."""
	with open(filename, 'r') as f:
		lines = f.readlines()
	
	ranges: list[str] = []
	ids: list[int] = []
	
	# Find the empty line separator
	separator_index = 0
	for i, line in enumerate(lines):
		trimmed = line.rstrip('\n')
		if not trimmed:
			separator_index = i
			break
		ranges.append(trimmed)
	
	# Collect individual IDs after the separator
	for line in lines[separator_index + 1:]:
		trimmed = line.rstrip('\n')
		if trimmed:
			ids.append(int(trimmed))
	
	return ranges, ids


def parse_ranges(range_strings: list[str]) -> list[tuple[int, int]]:
	"""Parse range strings into list of (lower, upper) tuples."""
	range_list: list[tuple[int, int]] = []
	for range_line in range_strings:
		lower, upper = map(int, range_line.split('-'))
		range_list.append((lower, upper))
		print(f"Fresh range: {lower} to {upper}")
	return range_list


def is_id_fresh(id_value: int, range_list: list[tuple[int, int]]) -> bool:
	"""Check if an ID falls within any of the fresh ranges."""
	for lower, upper in range_list:
		if lower <= id_value <= upper:
			return True
	return False


def count_fresh_available_ids(available_ids: list[int], range_list: list[tuple[int, int]]) -> int:
	"""Count how many available IDs are fresh."""
	fresh_count = 0
	for id_value in available_ids:
		is_fresh = is_id_fresh(id_value, range_list)
		status = "fresh" if is_fresh else "spoiled"
		print(f"Ingredient ID {id_value} is {status}")
		if is_fresh:
			fresh_count += 1
	return fresh_count


def main() -> None:
	# Parse input
	range_strings, available_ids = parse_input('input.txt')
	
	# Parse ranges into (lower, upper) tuples
	range_list = parse_ranges(range_strings)
	print()
	
	# Check which available IDs are fresh
	fresh_count = count_fresh_available_ids(available_ids, range_list)
	
	print()
	print(f"Answer: {fresh_count} of the available ingredient IDs are fresh")
	

if __name__ == "__main__":
	main() 
