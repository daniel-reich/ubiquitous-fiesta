
import numpy  
def total_volume(*boxes):
  return sum(list(map(lambda x:numpy.prod(x),boxes)))

