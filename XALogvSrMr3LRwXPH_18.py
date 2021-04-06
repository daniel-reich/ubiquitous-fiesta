
def is_shuffled_well(lst):
    import numpy as np
    diffs = np.diff(np.array(lst))
    return not any(abs(i)==abs(j)==1 for i,j in zip(diffs, diffs[1:]))

