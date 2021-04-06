
import numpy as np
def is_icecream_sandwich(txt):
  text = np.unique([x for x in txt])
  if len(txt) < 3:
    return False
  elif len(text) != 2:
    return False
  elif txt[0] != txt[-1]:
    return False
  elif txt == txt[::-1]:
    return True
  else:
    return False

