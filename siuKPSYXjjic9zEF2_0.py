
import math
def foil(length):
  diameter = 4
  while length > 0:
    length -= ((diameter) * math.pi)
    if length < 0:
      if (diameter * math.pi) / 2 < (length * (-1)):
        diameter += 0.0025
      else:
        diameter += 0.0025 * 2
    else:
      diameter += 0.0025 * 2
  return (round(diameter, 4))

