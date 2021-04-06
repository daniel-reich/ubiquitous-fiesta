
import math
​
​
def hex_color_mixer(colors):
  rgbs = []
  for color in colors:
    rgbs.append([int(color[1 + pair * 2:1 + pair * 2 + 2], 16) for pair in range(3)])
  new_color = []
  for index in range(3):
    val = sum(rgb[index] for rgb in rgbs) / len(rgbs)
    if val % 1 >= 0.5:
      val = math.ceil(val)
    else:
      val = int(round(val, 0))
    new_color.append('{:0>2X}'.format(val))
  return '#{}'.format(''.join(new_color))

