
import numpy as np
def total_volume(*boxes):
  return sum([np.prod(i) for i in boxes])

