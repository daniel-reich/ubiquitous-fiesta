
from math import ceil
​
def encryption(txt):
  txt = txt.replace(' ', '')
  
  row = ceil(len(txt)**.5)
  
  lst = [txt[x:x+row] for x in range(0, row**2, row)]
  
  return ' '.join(''.join(y[x] for y in lst if len(y) > x) \
                        for x in range(row))

