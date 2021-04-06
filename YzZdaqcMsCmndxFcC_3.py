
import numpy as np
​
​
def centroid(x1, y1, x2, y2, x3, y3):
  area = np.linalg.det(np.array([[x1, x2, x3], [y1, y2, y3], [1, 1, 1]]))
  if area == 0:
    return False
  return (round((x1+x2+x3)/3, 2), round((y1+y2+y3)/3, 2))

