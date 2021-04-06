
import numpy as np
def bugger(num):
    i = 0
    while len(str(num)) > 1:
        lst = [int(i) for i in str(num)]
        num = np.prod(lst)
        i += 1
    return i

