dial_num = 50 # Dial is from 0 to 99
nbm_time_passing_0 = 0

# read input_01.txt
with open('input.txt', 'r') as file:
	lines = file.readlines()
	# First letter in line is R or L, then the number of steps
	instructions = [(line[0], int(line[1:])) for line in lines]

for direction, steps in instructions:
	if direction == 'R':
		if (dial_num + steps) // 100 > 0:
			nbm_time_passing_0 += (dial_num + steps) // 100
		dial_num = (dial_num + steps) % 100

	elif direction == 'L':
		if (dial_num - steps) // 100 < 0: # Arrondi vers le bas
			nbm_time_passing_0 += abs((dial_num - steps) // 100)
		dial_num = (dial_num - steps) % 100

print(f"Number of times passing 0: {nbm_time_passing_0}")