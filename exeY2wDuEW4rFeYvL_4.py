
def ordered_matrix(a, b):
  import numpy as np
  return np.array([x for x in range(1,(a*b)+1)]).reshape(a,b).tolist()

