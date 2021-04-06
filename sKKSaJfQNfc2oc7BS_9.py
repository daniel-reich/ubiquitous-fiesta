
import numpy as np
def sle(m):
    a = np.array([m[0][:2], m[1][:2]])
    b = np.array([m[0][-1], m[1][-1]])
    try:
        return tuple(map(lambda x:round(x), np.linalg.solve(a,b)))
    except Exception as e:
        return False

