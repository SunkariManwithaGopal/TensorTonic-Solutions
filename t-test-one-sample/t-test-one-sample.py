import numpy as np

def t_test_one_sample(x, mu0):

    x = np.array(x, dtype=float)
    
    n = len(x)
    if n < 2:
        raise ValueError("Sample size must be at least 2.")
    mean = np.mean(x)
    std = np.std(x, ddof=1)
    t_stat = (mean - mu0) / (std / np.sqrt(n))
    
    return float(t_stat)
