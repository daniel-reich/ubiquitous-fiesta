
import numpy as np
def mystery_func(num):
  min_num = int(str(num)[0])
  max_num = int(str(num)[-1])
  
  return min_num * max_num * np.prod([int(x) for x in str(num)][1:-1])

