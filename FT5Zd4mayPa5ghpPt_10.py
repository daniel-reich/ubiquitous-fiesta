
def color_conversion(h):
  if type(h) == str:
    if '#' in h: h = h[1:]
    if len(h) != 6: return 'Invalid input!'
    try:
      ans = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
      return {'g': ans[1], 'r': ans[0], 'b': ans[2]}
    except:
      return 'Invalid input!'
  else:
    if (h['r'] < 0 or h['r'] > 255) or (h['g'] < 0 or h['g'] > 255) or (h['b'] < 0 or h['b'] > 255): return 'Invalid input!'
    return '#%02x%02x%02x' % (h['r'], h['g'], h['b'])

