
import re
​
def color_conversion(h):
  if isinstance(h, str):
    rgb = h.strip('#')
    if not re.match(r'^[a-f0-9]{6}$', rgb):
      return 'Invalid input!'
    red, green, blue = rgb[:2], rgb[2:4], rgb[4:]
    colors = []
    for color in (red, green, blue):
      value = int(color, base=16)
      if value < 0 or value > 255:
        return 'Invalid input!'
      colors.append(value)
    return {
      color: val
      for color, val in zip(['r', 'g', 'b'], colors)
    }
  else:
    order = ['r', 'g', 'b']
    colors = []
    for color, val in sorted(h.items(), key=lambda x: order.index(x[0])):
      if val < 0 or val > 255:
        return 'Invalid input!'
      colors.append('{:0>2x}'.format(val))
    return '#{}'.format(''.join(colors))

