
from math import floor
def repeated(s):
  for i in range(0, floor(len(s)/2)):
    if repeated_(s, s[:i+1]):
      return True
  return False
    
def repeated_(s, sub):
  step = len(sub)
  length = len(s)
  if length % step != 0:
    return False
  else:
    for i in range(0, length, step):
      if s[i:i+step] != sub:
        return False
    return True

