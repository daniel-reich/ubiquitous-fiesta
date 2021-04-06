
from math import factorial
def kempner(n):
  for i in range(1, n+1):
    if i == n:
      return n
    elif factorial(i)%n == 0:
      return i

