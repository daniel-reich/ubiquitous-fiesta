
import math
def find_vertex(x):
  y = [eval(i) for i in x.split('x')]
  return math.floor(-1*y[1]/(2*y[0]))

