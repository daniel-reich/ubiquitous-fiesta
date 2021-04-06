
import numpy as np
​
def can_see_stage(seats):
  seats = np.array(seats)
  return np.all(seats[1:] - seats[:-1] > 0)

