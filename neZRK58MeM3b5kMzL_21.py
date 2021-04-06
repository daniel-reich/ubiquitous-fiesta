
import numpy as np
​
def height_needed(volume):
  r = 5
  h = 3000*volume/(np.pi*r**2)
  return round(h,2)

