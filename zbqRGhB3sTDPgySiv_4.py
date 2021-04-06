
from math import factorial as f
def mod(base, key):
  return sum(f(i)%f(key) for i in range(min(base,key)))

