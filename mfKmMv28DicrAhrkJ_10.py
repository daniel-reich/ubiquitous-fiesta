
import math
​
def hex_color_mixer(colors):
  r = g = b = 0
  ll = len(colors)
  for color in colors:
    r += int(color[1:3], 16)
    g += int(color[3:5], 16)
    b += int(color[5:], 16)
    
  return '#%02X%02X%02X' % (math.floor(r/ll+0.5), math.floor(g/ll+0.5), math.floor(b/ll+0.5))

