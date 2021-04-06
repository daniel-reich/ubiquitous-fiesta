
import math
def is_circle_collision(c1, c2):
  return True if math.sqrt((c2[1] - c1[1])**2 + (c2[2] - c1[2])**2) < (c1[0] + c2[0]) else False

