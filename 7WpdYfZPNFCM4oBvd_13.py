
def is_magic(square):
    if len(square) == 0:
        return True
    import numpy as np
    square = np.array(square)
    if np.min(square) != 1:
        return False
    diag_sum = np.trace(square)
    diag_sum_ = np.trace(square[:, ::-1])
    if diag_sum != diag_sum:
        return False
    hor_sum = np.sum(square, axis=0)
    if (diag_sum == hor_sum).all() == False:
        return False
    ver_sum = np.sum(square, axis=1)
    if (diag_sum == ver_sum).all() == False:
        return False
    return True

