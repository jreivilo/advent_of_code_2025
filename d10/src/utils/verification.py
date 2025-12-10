"""
Solution verification utilities.
"""

from typing import List, Tuple


def verify_solution(solution: List[int], buttons: List[Tuple[int, ...]], 
                   targets: List[int], tolerance: float = 0.01) -> bool:
    """
    Verify that a solution correctly achieves the target values.
    
    Args:
        solution: list of button press counts
        buttons: list of button effects
        targets: list of target counter values
        tolerance: acceptable deviation from target
    
    Returns:
        True if solution is valid, False otherwise
    
    Example:
        solution=[2,3], buttons=[(0,1), (1,2)], targets=[2,5,3] -> True
        (counter 0: 2, counter 1: 2+3=5, counter 2: 3)
    """
    n_counters = len(targets)
    current = [0] * n_counters
    
    for btn_idx, press_count in enumerate(solution):
        for counter_idx in buttons[btn_idx]:
            current[counter_idx] += press_count
    
    for i, (curr, tgt) in enumerate(zip(current, targets)):
        if abs(curr - tgt) > tolerance:
            return False
    
    return True
