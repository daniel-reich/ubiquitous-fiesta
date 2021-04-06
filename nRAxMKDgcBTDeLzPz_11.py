
import numpy as np
def circular_shift(lst1, lst2, n):
    lst2 = list(np.roll(lst2,n))
    return lst1 == lst2

