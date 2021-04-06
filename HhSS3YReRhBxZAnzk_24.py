
import numpy
def gen_values(n, i):
  res = [round(i,2) for i in numpy.arange(0, n, i)]
  return res+[res[-1]+i] if res[-1]+i<=n else res

