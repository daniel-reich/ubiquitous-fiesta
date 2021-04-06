
import re
​
def color_conversion(h):
  if type(h) is str:
    if not bool(re.match('#?[0-9a-f]{6}$', h)): 
      return 'Invalid input!'
    r, g, b = re.findall('#?(..)(..)(..)', h)[0]
    return {'r': int(r, 16), 'g': int(g, 16), 'b': int(b, 16)}
  else:
    if any(i not in range(256) for i in h.values()): 
      return 'Invalid input!'
    return '#{:02x}{:02x}{:02x}'.format(h['r'], h['g'], h['b'])

