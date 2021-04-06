
import numpy
def total_volume(*boxes):
  return sum([numpy.prod(i) for i in boxes])

