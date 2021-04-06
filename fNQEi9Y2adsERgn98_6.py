
import numpy as np
def perimeter(lst):
  arr = np.array(lst)
  per = sum([np.linalg.norm((arr[i-1]-arr[i])) for i in range(len(arr))])
  return round(per,2)

