
import math
​
def group(lst, size):
  return([lst[i::math.ceil(len(lst)/size)] for i in range(math.ceil(len(lst)/size))])

