import heapq
from collections import Counter
import math

with open('input.txt') as f:
    map_3d = [tuple(map(int, line.split(','))) for line in f]

def euclidean_distance(p1, p2):
    """Calculate the straight-line (Euclidean) distance between two 3D points."""
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False  # Already in same circuit
        
        # Union by size
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x
        
        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        return True
    
    def get_circuit_sizes(self):
        circuits = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            if root not in circuits:
                circuits[root] = 0
            circuits[root] += 1
        return list(circuits.values())

# Calculate distances between all pairs of boxes
distances = []
n = len(map_3d)

for i in range(n):
    for j in range(i + 1, n):
        dist = euclidean_distance(map_3d[i], map_3d[j])
        distances.append((dist, i, j))

# Sort by distance
distances.sort()

# Create Union-Find structure
uf = UnionFind(n)

# Connect pairs until all boxes are in one circuit
num_circuits = n  # Start with n separate circuits
last_connection = None

for connection_num, (dist, i, j) in enumerate(distances, 1):
    if uf.union(i, j):
        num_circuits -= 1  # Successfully merged two circuits
        last_connection = (i, j, dist)
        
        if num_circuits == 1:
            # All boxes are now in a single circuit!
            print(f"All boxes unified at connection {connection_num}")
            print(f"Last connection: box {i} {map_3d[i]} <-> box {j} {map_3d[j]}")
            print(f"Distance: {dist:.2f}")
            break

# Calculate answer: multiply X coordinates
if last_connection:
    i, j, dist = last_connection
    x1 = map_3d[i][0]
    x2 = map_3d[j][0]
    answer = x1 * x2
    print(f"\nX coordinates: {x1} * {x2} = {answer}")
else:
    print("Error: Could not unify all boxes")
