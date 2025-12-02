dial_num = 50 # Dial is from 0 to 99
nbm_time_pointing_to_0 = 0

# read input_01.txt
with open('input.txt', 'r') as file:
	lines = file.readlines()
	# First letter in line is R or L, then the number of steps
	instructions = [(line[0], int(line[1:])) for line in lines]

for direction, steps in instructions:
	if direction == 'R':
		dial_num = (dial_num + steps) % 100
	elif direction == 'L':
		dial_num = (dial_num - steps) % 100

	if dial_num == 0:
		nbm_time_pointing_to_0 += 1

print(f"Number of times pointing to 0: {nbm_time_pointing_to_0}")