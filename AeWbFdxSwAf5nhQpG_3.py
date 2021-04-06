
import numpy
def persistence(num):
  x = 0
  while len(str(num))>1:
    num = numpy.prod([int(d) for d in str(num)])
    x += 1
  return x

