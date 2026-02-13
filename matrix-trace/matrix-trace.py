import numpy as np

def matrix_trace(A):
    A = np.array(A)
    n, m = A.shape
    
    total = 0
    for i in range(min(n, m)):
        total += A[i][i]
    
    return total



