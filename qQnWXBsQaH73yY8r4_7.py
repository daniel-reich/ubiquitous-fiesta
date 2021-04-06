
from math import factorial
def kempner(n):
  i = 1
  while(True):
    if factorial(i) % n == 0: return i
    i += 1

