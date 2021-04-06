
import numpy as np
def convert(slope):
  return 90 - round(np.degrees(np.arctan(slope)))

