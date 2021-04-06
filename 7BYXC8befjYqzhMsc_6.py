
def classify_rug(pattern):
  import numpy as np
  horz, vert = False, False
  if np.array_equal(pattern, np.flip(pattern, 0)):
    horz = True
  if np.array_equal(pattern, np.flip(pattern, 1)):
    vert = True
  if horz and vert:
    return "perfect"
  elif horz:
    return "horizontally symmetric"
  elif vert:
    return "vertically symmetric"
  else:
    return "imperfect"

