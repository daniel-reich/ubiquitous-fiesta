
import math;
def is_parallelogram(x):
  x.sort();
  return math.hypot((x[1][0]-x[0][0]),(x[1][1] - x[0][1])) == math.hypot((x[3][0]-x[2][0]),(x[3][1] - x[2][1]))

