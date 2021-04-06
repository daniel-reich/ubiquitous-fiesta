
import re
def color_conversion(h):
  if isinstance(h, dict):
    if all(v in range(256) for v in h.values()):
      return '#{:02x}{:02x}{:02x}'.format(h['r'], h['g'], h['b'])
  elif isinstance(h, str):
    if re.match('#*[a-fA-F0-9]{6}$', h):
      h = h.strip('#')
      R, G, B = [int(h[i:i+2], 16) for i in range(0, 6, 2)]
      return {'r':R, 'g':G, 'b':B}
  return 'Invalid input!'

