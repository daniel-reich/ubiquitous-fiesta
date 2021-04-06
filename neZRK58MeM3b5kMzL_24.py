
import math
def height_needed(volume):
  # volume = 1/3 pi r * r * h
  return round(volume / (25 * math.pi) * 3000, 2)

