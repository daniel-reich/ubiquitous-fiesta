
import re
def hex2rgb(hex):
  m = re.match(r"^#?([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})$", hex)
  if m:
    r, g, b = m.group(1), m.group(2), m.group(3)
    return {'r':int(r, 16), 'g':int(g, 16), 'b':int(b, 16)}
  else:
    return "Invalid input!"
​
def rgb2hex(rgb):
  if all(0 <= v and v <= 255 for v in rgb.values()):
    return '#{:02x}{:02x}{:02x}'.format(rgb['r'], rgb['g'], rgb['b'])
  else:
    return "Invalid input!"
​
def color_conversion(h):
  if isinstance(h, str):
    return hex2rgb(h)
  else:
    return rgb2hex(h)

