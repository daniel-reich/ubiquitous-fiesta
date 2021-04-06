
import numpy as np
def reversed_binary_integer(num):
  s = bin(num)[2:][::-1]
  n = 0
  for i in s:
    i = int(i)
    n = n*2+i
  return n

