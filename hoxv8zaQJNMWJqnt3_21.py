
import numpy as np
def is_heteromecic(num):
    if num == 0:
        return(True)
    elif(any(i*(i+1) == num for i in range(1, int(np.ceil(num/2))+1))):
        return(True)
    else:
        return(False)

