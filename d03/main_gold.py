total_voltage = 0
total_battery_to_switch = 12

with open('input.txt', 'r') as f:
	lines = f.readlines()

for line in lines:
	# Remove trailing newline and skip empty lines
	trimmed = line.rstrip('\n')
	if not trimmed:
		continue

	voltage_value = ''

	# Convert each character to an integer
	digits = [int(ch) for ch in trimmed]

	nb_batteries_used = 0
	while nb_batteries_used < total_battery_to_switch:
		highest_number = max(digits[:-(total_battery_to_switch - nb_batteries_used - 1)] if total_battery_to_switch - nb_batteries_used - 1 > 0 else digits)
		voltage_value += str(highest_number)
		# Trim the digits list to only consider the part after the found highest number
		highest_index = digits.index(highest_number)
		digits = digits[highest_index + 1:]
		nb_batteries_used += 1

	print(f"Voltage value for line '{trimmed}': {voltage_value} with length {len(voltage_value)}")
	total_voltage += int(voltage_value)

print(f"Total voltage: {total_voltage} with length {len(str(total_voltage))}")