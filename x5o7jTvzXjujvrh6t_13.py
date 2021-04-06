
import math as m
def i_sqrt(n):
  num = n
  cont = 0
  if n < 0:
    return 'invalid'
  if n < 2:
    return 0
  while True:
    cont += 1
    s = m.sqrt(num)
    num = s
    if s < 2:
      return cont

