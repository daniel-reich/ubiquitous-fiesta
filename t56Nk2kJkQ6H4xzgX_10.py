
def swap_xy(txt):
​
  indexes = []
  index = []
​
  for n in range(0, len(txt)):
    i = txt[n]
​
    if i == '(':
      index.append(n + 1)
    
    if i == ')':
      index.append(n)
      indexes.append(index)
      index = []
  
  xys = []
​
  for index in indexes:
​
    xindex = int(index[0])
    yindex = int(index[1])
​
    s = ''
​
    for n in range(xindex, yindex):
      s += txt[n]
​
    xys.append(s)
  
  nxys = []
​
  for xy in xys:
    l = list(reversed(xy.split(', ')))
    nxys.append(l)
  
  xys = nxys
  del nxys
​
  template = '({}, {})'
​
  tr = []
​
  for xy in xys:
    x = xy[0]
    y = xy[1]
​
    t = template.format(x, y)
​
    tr.append(t)
  
  return ', '.join(tr)

