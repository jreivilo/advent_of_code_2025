"""
Matrix building utilities.
"""

from typing import List, Tuple
import numpy as np


def build_matrix(n_counters: int, buttons: List[Tuple[int, ...]]) -> np.ndarray:
    """
    Build coefficient matrix A where A[i][j] = 1 if button j affects counter i.
    
    Args:
        n_counters: number of counters
        buttons: list of button effects (each button is a tuple of counter indices)
    
    Returns:
        Matrix A of shape (n_counters, n_buttons) where A @ x = target
    
    Example:
        n_counters=4, buttons=[(0,1), (2,3)] -> A = [[1,0], [1,0], [0,1], [0,1]]
    """
    n_buttons = len(buttons)
    A = np.zeros((n_counters, n_buttons), dtype=int)
    
    for j, button in enumerate(buttons):
        for i in button:
            A[i][j] = 1
    
    return A
