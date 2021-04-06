
import numpy as np
def rotate_transform(arr, num):
  return np.rot90(np.array(arr),k = -1 * num % 4).tolist()

