"""
Day 10: Button Light Configuration Solver

This solution uses BFS with bit manipulation to find the minimum button presses
needed to configure indicator lights on machines.

Key optimizations:
- Bit manipulation: lights represented as integers (0/1 bits)
- BFS: guarantees finding minimum presses
- State caching: avoids revisiting configurations
"""

import re
from collections import deque
from typing import List, Tuple


def parse_machine(line: str) -> Tuple[int, int, List[int]]:
    """
    Parse a machine configuration line.
    
    Args:
        line: Input line containing [lights] (buttons...) {joltage}
    
    Returns:
        tuple: (target_state, num_lights, button_masks)
            - target_state: integer with bits representing desired light state
            - num_lights: total number of lights
            - button_masks: list of integers, each representing which lights a button toggles
    """
    # Extract indicator lights pattern [.##.]
    lights_match = re.search(r'\[([\.\#]+)\]', line)
    if not lights_match:
        raise ValueError(f"Cannot find lights pattern in line: {line}")
    
    lights_pattern = lights_match.group(1)
    num_lights = len(lights_pattern)
    
    # Convert target pattern to bit representation
    # '#' = 1 (on), '.' = 0 (off)
    target_state = 0
    for i, char in enumerate(lights_pattern):
        if char == '#':
            target_state |= (1 << i)
    
    # Extract button configurations (0,1,2) (3,4) etc.
    buttons = []
    button_pattern = r'\(([0-9,]+)\)'
    for match in re.finditer(button_pattern, line):
        button_indices = [int(x) for x in match.group(1).split(',')]
        
        # Convert button to bit mask
        button_mask = 0
        for idx in button_indices:
            button_mask |= (1 << idx)
        
        buttons.append(button_mask)
    
    return target_state, num_lights, buttons


def solve_machine(target_state: int, num_lights: int, buttons: List[int]) -> int:
    """
    Find minimum button presses to reach target state using BFS.
    
    Args:
        target_state: desired light configuration as bit integer
        num_lights: total number of lights
        buttons: list of button masks (bit representations)
    
    Returns:
        Minimum number of button presses, or -1 if impossible
    """
    # All lights start off (state = 0)
    initial_state = 0
    
    # If already at target, no presses needed
    if initial_state == target_state:
        return 0
    
    # BFS: (current_state, num_presses)
    queue = deque([(initial_state, 0)])
    visited = {initial_state}
    
    while queue:
        current_state, presses = queue.popleft()
        
        # Try pressing each button
        for button_mask in buttons:
            # Toggle lights affected by this button (XOR operation)
            next_state = current_state ^ button_mask
            
            # Check if we reached target
            if next_state == target_state:
                return presses + 1
            
            # Add to queue if not visited
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, presses + 1))
    
    # Target unreachable
    return -1


def main():
    """Main solver for all machines."""
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    
    total_presses = 0
    
    for i, line in enumerate(lines, 1):
        target_state, num_lights, buttons = parse_machine(line)
        
        min_presses = solve_machine(target_state, num_lights, buttons)
        
        if min_presses == -1:
            print(f"Machine {i}: IMPOSSIBLE")
        else:
            print(f"Machine {i}: {min_presses} presses")
            total_presses += min_presses
    
    print(f"\nTotal button presses required: {total_presses}")


if __name__ == "__main__":
    main()