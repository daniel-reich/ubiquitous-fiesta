
import numpy as np
​
def rotate_transform(arr, num):
    return np.rot90(arr, -num).tolist()

