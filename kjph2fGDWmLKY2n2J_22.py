
import re
​
def valid_color (color):
  if re.match('rgba? +\(', color): 
    return False
    
  color = ''.join(ch for ch in color if ch not in '   ')
  has_a, r, g, b, a = re.findall('rgb(a)?\(({0})?,({0})?,({0})?(?:,({0}))?\)'.format('[\d.-]+%?'), color)[0]
  
  if (has_a and not 0 <= float(a or -1) <= 1) or (not has_a and a): 
    return False
  
  per = all(i.endswith('%') and 0 <= float(i[:-1]) <= 100 for i in (r, g, b))
  hxd = all(i.isnumeric() and 0 <= float(i) <= 255 for i in (r, g, b))
  
  return per or hxd

