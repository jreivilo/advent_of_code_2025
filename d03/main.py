total_voltage = 0

with open('input.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    # Remove trailing newline and skip empty lines
    trimmed = line.rstrip('\n')
    if not trimmed:
        continue

    # Convert each character to an integer
    digits = [int(ch) for ch in trimmed]

    # Find the highest number in the line without the last digit
    first_highest_number = max(digits[:-1])

    # Find the second highest number in the line that appears after the highest number
    highest_index = digits.index(first_highest_number)
    second_highest_number = max(digits[highest_index + 1:]) if highest_index + 1 < len(digits) else 0

    # Concatenate the highest and second highest numbers to form a voltage value
    voltage_value = int(f"{first_highest_number}{second_highest_number}")
    total_voltage += voltage_value

print(total_voltage)
