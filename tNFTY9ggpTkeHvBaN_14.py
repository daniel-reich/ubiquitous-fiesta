
import numpy
def total_volume(*boxes):
  return sum( [numpy.product(i) for i in boxes] )

