import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    a = np.asarray(a)
    b = np.asarray(b)

    # Validate dimensions
    if a.ndim != 1 or b.ndim != 1:
        raise ValueError("Inputs must be 1D NumPy arrays.")
    if a.shape[0] != b.shape[0]:
        raise ValueError("Arrays must have the same length.")

    dot = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    # Handle zero vectors gracefully
    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0

    return float(dot / (norm_a * norm_b))

    pass