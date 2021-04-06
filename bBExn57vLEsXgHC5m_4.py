
import numpy as np
def same_line(lst):
  x = [point[0] for point in lst]
  y = [point[1] for point in lst]
  
  x2 = x[1::]
  y2 = y[1::]
  unix = np.unique(x)
  uniy = np.unique(y)
  
  if len(unix) == 1 or len(uniy) == 1:
    return True
  elif len(unix) == 2 or len(uniy) == 2:
    return False
  else:
    slopes = [(y1 - y[0])/(x1 - x[0]) for x1, y1 in zip(x2,y2)]
    if slopes[0] == slopes[1]:
      return True
    else:
      return False

