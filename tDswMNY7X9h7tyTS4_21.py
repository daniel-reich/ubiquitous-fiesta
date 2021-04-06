
import math
def pascals_triangle(n):
  l=[]
  for i in range(n):
    for j in range(i+1):
      l.append(math.factorial(i)//(math.factorial(j)*math.factorial(i-j)))
  return l

