
from math import floor
​
#Moivre-Binet
def fib(n):
  return floor(1/5**.5*(((1+5**.5)/2)**n - ((1-5**.5)/2)**n))

