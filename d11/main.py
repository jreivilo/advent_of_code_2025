#!/usr/bin/env python3
"""Day 11: Reactor - Find all paths from 'you' to 'out'"""

def parse_input(filename):
    """Parse the input file and build a graph as an adjacency list."""
    graph = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            # Parse "device: output1 output2 ..."
            parts = line.split(': ')
            device = parts[0]
            outputs = parts[1].split() if len(parts) > 1 else []
            graph[device] = outputs
    
    return graph


def count_paths(graph, start, end, visited=None):
    """Count all paths from start to end using DFS."""
    if visited is None:
        visited = set()
    
    # Base case: reached the end
    if start == end:
        return 1
    
    # If this node has no outgoing edges, no path exists
    if start not in graph:
        return 0
    
    # Mark current node as visited
    visited.add(start)
    
    total_paths = 0
    for neighbor in graph[start]:
        # Only visit if not already in current path (avoid cycles)
        if neighbor not in visited:
            total_paths += count_paths(graph, neighbor, end, visited)
    
    # Backtrack: unmark current node
    visited.remove(start)
    
    return total_paths


def main():
    # Test with example
    example = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""
    
    # Parse example
    graph = {}
    for line in example.strip().split('\n'):
        parts = line.split(': ')
        device = parts[0]
        outputs = parts[1].split()
        graph[device] = outputs
    
    # Test with example
    num_paths = count_paths(graph, 'you', 'out')
    print(f"Example: {num_paths} paths from 'you' to 'out'")
    assert num_paths == 5, f"Expected 5, got {num_paths}"
    
    # Solve actual problem
    graph = parse_input('input.txt')
    num_paths = count_paths(graph, 'you', 'out')
    print(f"Answer: {num_paths} paths from 'you' to 'out'")


if __name__ == '__main__':
    main()
