import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    A = np.array(A, dtype=float)
    
    if A.ndim != 2:
        return None
    
    n, m = A.shape
    if n != m:
        return None
    
    if np.isclose(np.linalg.det(A), 0.0):
        return None
    
    A_inv = np.linalg.inv(A)
    
    return A_inv
