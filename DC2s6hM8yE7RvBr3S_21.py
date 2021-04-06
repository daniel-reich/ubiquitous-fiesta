
import numpy as np
def subtract_matrix(lst1, lst2):
    lst1 = [list(map(float, l)) for l in lst1]
    lst2 = [list(map(float, l)) for l in lst2]
    return np.subtract(np.array(lst1), np.array(lst2)).tolist()

