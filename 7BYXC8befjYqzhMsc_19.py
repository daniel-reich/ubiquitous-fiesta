
import numpy as np
​
def check(pat):
  for a in pat:
    a = ''.join(a)
    if not a.endswith(a[:len(a)//2]):
      return 1
  return 0
      
def classify_rug(pattern):
  pat = np.array(pattern)
  ver, hor = check(pat), check(np.rot90(pat))
  if hor == 0 == ver:
    return "perfect"
  elif hor == 1 == ver:
    return "imperfect"
  elif ver == 1:
    return "horizontally symmetric"
  return "vertically symmetric"

