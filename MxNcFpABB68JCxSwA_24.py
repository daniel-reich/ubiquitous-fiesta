
from math import floor
def legendre(p, n):
  i=1
  somme = 0
  while floor(n/p**i) > 0:
    somme += floor(n/p**i)
    i += 1
  return somme

