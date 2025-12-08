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

# Use 10 connections for testing
num_connections = 1000

# Create Union-Find structure
uf = UnionFind(n)

# Connect the closest pairs
for connection_num, (dist, i, j) in enumerate(distances[:num_connections], 1):
    if uf.union(i, j):
        print(f"Connection {connection_num}: box {i} {map_3d[i]} <-> box {j} {map_3d[j]} (dist: {dist:.2f})")
    else:
        print(f"Connection {connection_num}: box {i} and box {j} already in same circuit (skipped)")

# Get circuit sizes
circuit_sizes = uf.get_circuit_sizes()
circuit_sizes.sort(reverse=True)

print(f"\nTotal circuits: {len(circuit_sizes)}")
print(f"Circuit sizes: {circuit_sizes}")
print(f"Three largest circuits: {circuit_sizes[:3]}")

# Calculate answer
answer = circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]
print(f"\nAnswer (product of three largest): {answer}")
