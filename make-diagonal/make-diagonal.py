import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    v=np.array(v)
    m=v.size
    h=np.zeros((m,m),dtype=v.dtype)
    for i in range(m):
        h[i,i]=v[i]
    return h
    pass
