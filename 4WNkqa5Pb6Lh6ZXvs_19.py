
import re
​
def evaluate_polynomial(poly, num):
  if '&' in poly or '//' in poly: return 'invalid'
  poly = poly.replace('x', str(num))
  if '^' in poly:
    s = poly.split('^')
    if len(s[0]) == 2:
      s[0] = s[0][:1] + '*' + s[0][1]
    poly = '**'.join(s)
  elif '(' in poly:
    poly = poly.replace('(', '*(')
  
  try: 
    return eval(poly)
  except:
    return 'invalid'
  
  #poly = poly.replace('(', '*(').replace('x', str(num))
  #print(poly, eval(poly))
  #t = re.sub('[0-9]+[x]', '[0-9]+[*][x|(]', poly)

