
import numpy as np
def matrix_multiply(a, b):
    try:
        return np.dot(a, b).tolist()
    except ValueError:
        return "invalid"

