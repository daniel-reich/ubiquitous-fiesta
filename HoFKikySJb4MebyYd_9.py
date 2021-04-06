
import numpy as np
def transform_matrix(lst):
    result = []; counter = 0
    lst = np.array(lst)
    while counter < len(lst[:,0]): 
        result.append([sum(lst[counter,:]) + sum(lst[:,n]) - (lst[counter,n])*2 for n in range(len(lst[0,:]))])
        counter += 1
    return result

