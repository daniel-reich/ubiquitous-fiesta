
import math
import numpy
import sys
​
def bell(n):
  c = {}
  c[0,0] = 1
  for i in range(1,n):
    c[i,0] = c[i-1,i-1]
    for j in range(1,i+1):
      c[i,j] = c[i-1,j-1]+c[i,j-1]
  return c[n-1,n-1]

