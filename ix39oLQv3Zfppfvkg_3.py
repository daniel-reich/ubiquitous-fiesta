
import numpy as np
def multiply_matrix(m1, m2):
    try:
        ans =np.dot(np.array(m1),np.array(m2))
    except  ValueError:
        return  'ERROR'
    return list(map(lambda x:list(x),list(ans)))

