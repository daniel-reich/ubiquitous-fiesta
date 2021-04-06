
import numpy as np
def max_product(n):
  maximum = max([np.prod([int(y) for y in str(x)]) for x in range(n+1)])
  x = [x for x in range(n+1) if np.prod([int(y) for y in str(x)]) == maximum]
  return x

