
def matrix_multiply(a, b):
    import numpy as np
    try:  
        result=np.matmul(a, b)
        return result.tolist()
    except ValueError:
        return "invalid"

