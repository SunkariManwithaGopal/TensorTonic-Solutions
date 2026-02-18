import numpy as np

def chi2_independence(C):
    C = np.array(C, dtype=float)
    
    row_sums = C.sum(axis=1, keepdims=True)
    col_sums = C.sum(axis=0, keepdims=True)
    total = C.sum()
    
    expected = (row_sums @ col_sums) / total
    chi2 = np.sum((C - expected) ** 2 / expected)
    
    return float(chi2), expected
