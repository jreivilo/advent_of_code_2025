"""
Mixed Integer Linear Programming (MILP) solver.

Finds the optimal integer solution that minimizes button presses.
Uses scipy.optimize.milp with branch & bound algorithm.

This guarantees the MINIMUM number of button presses needed.
"""

from typing import List, Tuple, Optional
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

from .utils import verify_solution


def solve_milp(target: List[int], buttons: List[Tuple[int, ...]], 
               A: np.ndarray) -> Tuple[int, Optional[List[int]], str]:
    """
    Solve using Mixed Integer Linear Programming.
    
    This finds the OPTIMAL integer solution by solving:
        minimize: sum(x)
        subject to: A @ x = target
                    x >= 0
                    x are integers
    
    Args:
        target: list of target counter values
        buttons: list of button effects
        A: coefficient matrix
    
    Returns:
        (total_presses, solution, method)
    """
    n_buttons = len(buttons)
    b = np.array(target, dtype=float)
    
    try:
        # Objective: minimize sum of button presses
        c = np.ones(n_buttons)
        
        # Constraints: A @ x = target (equality)
        constraints = LinearConstraint(A, lb=b, ub=b)
        
        # Bounds: x >= 0
        bounds = Bounds(lb=np.zeros(n_buttons), ub=np.inf)
        
        # All variables are integers
        integrality = np.ones(n_buttons)
        
        # Solve MILP with strict optimality requirements
        result = milp(c=c, constraints=constraints, bounds=bounds,
                     integrality=integrality, 
                     options={
                         'disp': False,
                         'time_limit': 10.0,  # 10 seconds max per machine
                         'presolve': False,
                         'mip_rel_gap': 1 # Require exact optimal (no gap)
                     })
        
        if result.success:
            x_solution = np.round(result.x).astype(int)
            x_solution = np.maximum(x_solution, 0)
            
            # Verify solution
            if verify_solution(x_solution.tolist(), buttons, target):
                return (int(np.sum(x_solution)), x_solution.tolist(), "milp")
            else:
                return (-1, None, "milp-verify-failed")
        else:
            return (-1, None, "milp-no-solution")
    
    except Exception as e:
        return (-1, None, f"milp-error")
