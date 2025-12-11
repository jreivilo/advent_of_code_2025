#!/usr/bin/env python3
"""Day 11 Part 2: Reactor - Find paths from 'svr' to 'out' that visit both 'dac' and 'fft'"""
from functools import lru_cache

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


def count_paths_optimized(graph, start, end, required_nodes):
    """
    Count paths using dynamic programming with memoization.
    State: (current_node, which_required_nodes_have_been_visited)
    """
    # Convert graph values to tuples for hashing
    graph_frozen = {k: tuple(v) for k, v in graph.items()}
    required_frozen = frozenset(required_nodes)
    
    @lru_cache(maxsize=None)
    def dp(node, visited_required):
        """
        Count paths from node to end, given we've already visited visited_required nodes.
        visited_required is a frozenset of required nodes visited before reaching this node.
        """
        # Check if current node is required
        new_visited = visited_required
        if node in required_frozen:
            new_visited = visited_required | {node}
        
        # Base case: reached the end
        if node == end:
            return 1 if new_visited == required_frozen else 0
        
        # No outgoing edges
        if node not in graph_frozen:
            return 0
        
        # Sum paths through all neighbors
        total = 0
        for neighbor in graph_frozen[node]:
            total += dp(neighbor, new_visited)
        
        return total
    
    return dp(start, frozenset())


def main():
    # Test with example
    example = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""
    
    # Parse example
    graph = {}
    for line in example.strip().split('\n'):
        parts = line.split(': ')
        device = parts[0]
        outputs = parts[1].split()
        graph[device] = outputs
    
    # Test with example
    required_nodes = {'dac', 'fft'}
    num_paths = count_paths_optimized(graph, 'svr', 'out', required_nodes)
    print(f"Example: {num_paths} paths from 'svr' to 'out' visiting both 'dac' and 'fft'")
    assert num_paths == 2, f"Expected 2, got {num_paths}"
    
    # Solve actual problem
    graph = parse_input('input.txt')
    required_nodes = {'dac', 'fft'}
    num_paths = count_paths_optimized(graph, 'svr', 'out', required_nodes)
    print(f"Answer: {num_paths} paths from 'svr' to 'out' visiting both 'dac' and 'fft'")


if __name__ == '__main__':
    main()
