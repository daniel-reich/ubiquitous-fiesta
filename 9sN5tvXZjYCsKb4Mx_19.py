
def cube_diagonal(volume):
  import math
  side = float(volume **(1/3))
  diagonal_base = (2*side*side)**(1/2)
  diagonal = (diagonal_base**2 + side**2)**(1/2)
  return round(diagonal, 2)

