
def cars(wheels, bodies, figures):
  import math
  return min([math.floor(wheels/4), bodies, math.floor(figures/2)])

