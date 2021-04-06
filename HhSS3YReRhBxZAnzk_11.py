
import numpy as np
​
def gen_values(n, i):
  return [round(i,2) for i in np.arange(0, n+0.001, i)]

