import numpy as np

def percentiles(x, q):
    x = np.sort(np.array(x, dtype=float))
    q = np.array(q, dtype=float)
    
    n = len(x)
    idx = (n - 1) * q / 100.0
    
    lower = np.floor(idx).astype(int)
    upper = np.ceil(idx).astype(int)
    
    weight = idx - lower
    
    return (1 - weight) * x[lower] + weight * x[upper]
