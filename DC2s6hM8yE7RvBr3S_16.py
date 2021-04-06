
import numpy as np
def subtract_matrix(lst1, lst2):
    lst1 = list(map(lambda x:list(map(lambda y:int(y),x)),np.array(lst1)))
    lst2 = list(map(lambda x:list(map(lambda y:float(y),x)),np.array(lst2)))
    ans = list(np.subtract(lst1,lst2))
    return list(map(lambda x:list(x), ans))

