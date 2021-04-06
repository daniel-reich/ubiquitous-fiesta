
# New code
import numpy as np
​
def help_bobby(size):  
    array = np.zeros((size,size)).astype(int)
    array = array.tolist()
​
    for i in range(size):
        array[i][i] = 1
        array[i][size - i - 1] = 1
​
    return array

