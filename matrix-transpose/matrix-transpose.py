import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A = np.array(A)              # Ensure input is NumPy array
    rows, cols = A.shape         # Original shape (N, M)
    
    result = np.zeros((cols, rows), dtype=A.dtype) # New shape (M, N)
    
    for i in range(rows):
        for j in range(cols):
            result[j][i] = A[i][j]
    
    return result
