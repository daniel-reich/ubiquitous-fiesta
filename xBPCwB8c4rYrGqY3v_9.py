
import numpy as np
def missing(lst):
    full_lst = [i for i in np.linspace(lst[0],lst[-1],len(lst)+1)]
    return [i for i in full_lst if i not in lst][0]

