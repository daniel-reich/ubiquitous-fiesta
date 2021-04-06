
from numpy import prod
def bugger(num):
  i=0
  while num>9:
    num = prod([int(n) for n in str(num)])
    i+=1
  return i

