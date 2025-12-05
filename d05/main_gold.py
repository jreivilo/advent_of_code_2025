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


def merge_ranges(range_list: list[tuple[int, int]]) -> list[tuple[int, int]]:
	"""Merge overlapping ranges to get unique coverage."""
	if not range_list:
		return []
	
	# Sort ranges by lower bound
	sorted_ranges = sorted(range_list)
	merged: list[tuple[int, int]] = [sorted_ranges[0]]
	
	for lower, upper in sorted_ranges[1:]:
		last_lower, last_upper = merged[-1]
		
		# Check if current range overlaps or is adjacent to the last merged range
		if lower <= last_upper + 1:
			# Merge by extending the upper bound if needed
			merged[-1] = (last_lower, max(last_upper, upper))
		else:
			# No overlap, add as new range
			merged.append((lower, upper))
	
	return merged


def count_total_fresh_ids(range_list: list[tuple[int, int]]) -> int:
	"""Count total unique IDs covered by all ranges."""
	merged = merge_ranges(range_list)
	
	total = 0
	print("\nMerged ranges:")
	for lower, upper in merged:
		count = upper - lower + 1
		print(f"  {lower}-{upper}: {count} IDs")
		total += count
	
	return total


def main() -> None:
	# Parse input
	range_strings, _available_ids = parse_input('input.txt')
	
	# Parse ranges into (lower, upper) tuples
	range_list = parse_ranges(range_strings)
	
	# Count total unique fresh IDs
	total_fresh = count_total_fresh_ids(range_list)
	
	print(f"\n Answer: {total_fresh} ingredient IDs are considered fresh")



if __name__ == "__main__":
	main() 
