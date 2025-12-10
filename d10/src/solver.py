"""
Main solver orchestration.
"""

from typing import List, Tuple

from .utils import build_matrix, verify_solution
from .milp_solver import solve_milp


def solve_machine(targets: List[int], buttons: List[Tuple[int, ...]]) -> Tuple[int, List[int], str]:
    """
    Solve using MILP only for guaranteed optimal solution.
    
    MILP (Mixed Integer Linear Programming) finds the integer solution
    that minimizes sum(x) subject to A·x = target.
    
    This guarantees we find the MINIMUM number of button presses.
    
    Args:
        targets: list of target counter values
        buttons: list of button effects
    
    Returns:
        (total_presses, solution, method) where:
            - total_presses: sum of button presses (-1 if failed)
            - solution: list of button press counts
            - method: string describing which method succeeded
    """
    n_counters = len(targets)
    n_buttons = len(buttons)
    
    # Build coefficient matrix
    A = build_matrix(n_counters, buttons)
    
    # Solve with MILP (guaranteed optimal)
    total, solution, method = solve_milp(targets, buttons, A)
    if total != -1:
        return (total, solution, method)
    
    # Failed
    return (-1, [], "milp-failed")
