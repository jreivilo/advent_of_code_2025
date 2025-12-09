with open('input.txt') as f:
    lines = f.read().strip().split('\n')

# Parse coordinates
coordinates = []
for line in lines:
    x, y = map(int, line.split(','))
    coordinates.append((x, y))

# Find largest rectangle area
max_area = 0

for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[j]
        
        # Calculate rectangle area
        area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
        
        if area > max_area:
            max_area = area

print(max_area)
    