
from numpy import prod
def persistence(num):
  s,i = str(num),0
  while len(s)>1:
    s = str(prod([int(x) for x in s]))
    i+=1
  return i

