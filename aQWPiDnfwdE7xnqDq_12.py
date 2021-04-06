
import numpy
def drange(a = 0, b = 0, c = 0):
  ans = []
  if a != 0 and b == 0 and c == 0:
    for i in range(a):
      if type(i) == float:
        ans.append(round(i,2))
      ans.append(i)
    return tuple(ans)
  if a != 0 and b != 0 and c == 0:
    for i in range(a,b):
      if type(i) == float:
        ans.append(round(i,2))
      ans.append(i)
    return tuple(ans)
  if a != 0 and b != 0 and c != 0:
    for i in numpy.arange(a,b,c):
      ans.append(round(i,3))
    return tuple(ans)

