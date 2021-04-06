
import numpy as np
​
def gen_values(n, i):
  return [round(v, 2) for v in np.arange(0, n + 0.01, i)]

