
from numpy import sign
​
def id_mtrx(n):
  try:
    return [[int(i == j) for i in range(abs(n))] for j in range(abs(n))][::sign(n)]
  except:
    return 'Error'

