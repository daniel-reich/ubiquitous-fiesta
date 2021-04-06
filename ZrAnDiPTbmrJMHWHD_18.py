
from re import findall 
def is_central(s):
  if not len(s) % 2:
    return False
  string = '\S'
  x = s.index(findall(string, s)[0])
  length = len(s) // 2
  return length == x

