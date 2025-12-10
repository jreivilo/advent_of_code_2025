"""
Input parsing utilities.
"""

import re
from typing import List, Tuple


def parse_machine(line: str) -> Tuple[List[int], List[Tuple[int, ...]]]:
    """
    Parse machine configuration from input line.
    
    Args:
        line: Format: [lights] (button1) (button2) ... {joltage1,joltage2,...}
    
    Returns:
        (target_values, button_effects) where:
            - target_values: list of target counter values
            - button_effects: list of tuples, each tuple contains counter indices a button affects
    
    Example:
        "[.##.] (3) (1,3) (2) {3,5,4,7}" -> ([3,5,4,7], [(3,), (1,3), (2,)])
    """
    joltage_match = re.search(r'\{([0-9,]+)\}', line)
    if not joltage_match:
        raise ValueError(f"No joltage pattern found: {line}")
    
    targets = [int(x) for x in joltage_match.group(1).split(',')]
    
    buttons = [
        tuple(int(x) for x in match.group(1).split(','))
        for match in re.finditer(r'\(([0-9,]+)\)', line)
    ]
    
    return targets, buttons
