
import numpy as np
def can_enter_cave(x):
    if len(x[0]) == 1:
        return True
    else:
        nx = np.array(x)
        curr = nx[:,0]
        next = nx[:,1]
        for i in range(len(curr)):
            if curr[i] == 0 and next[i] == 0:
                return can_enter_cave(nx[:,1:])
        return False

