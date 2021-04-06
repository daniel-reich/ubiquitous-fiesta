
import re
​
def color_conversion(h):
  to_hex = lambda n: ('0'+hex(n)[2:])[-2:]
  if type(h) is dict:
    r, g, b = h['r'], h['g'], h['b']
    if any([x < 0 or 255 < x for x in [r, g, b]]): return 'Invalid input!'
    return '#{}{}{}'.format(to_hex(r), to_hex(g), to_hex(b))
  if not bool(re.search(r'\A#?[0-9a-f]{6}\Z', h)): return 'Invalid input!'
  r, g, b = re.findall(r'(?:.{2})', h.strip('#'))
  return {'r': int('0x'+r, 16), 'g': int('0x'+g, 16), 'b': int('0x'+b, 16)}

