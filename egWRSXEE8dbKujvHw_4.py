
from math import sqrt
def is_circle_collision(c1, c2):
    x = sqrt((c1[1] - c2[1])**2 + (c1[-1] - c2[-1])**2)
    if x < c1[0] + c2[0]:
      return True
    return False

