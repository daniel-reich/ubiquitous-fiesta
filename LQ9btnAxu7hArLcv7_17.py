
def diagonalize(n, d):
  def convert_2_ur(ul):
​
    ur = []
​
    for row in ul:
      r = list(reversed(row))
      ur.append(r)
    
    return ur
  def convert_2_ll(ul):
​
    ll = []
​
    for n in reversed(range(0, len(ul))):
      row = ul[n]
      ll.append(row)
    
    return ll
  def convert_2_lr(ul):
​
    lr = []
​
    for n in reversed(range(0, len(ul))):
      row = list(reversed(ul[n]))
      lr.append(row)
    
    return lr
​
  rows = []
  bn = 0
  en = n
​
  while len(rows) != n:
    rows.append(list(range(bn, en)))
    bn += 1
    en += 1
  
  if d == 'ul':
    return rows
  elif d == 'ur':
    c2ur = convert_2_ur(rows)
    return c2ur
  elif d == 'll':
    c2ll = convert_2_ll(rows)
    return c2ll
  elif d == 'lr':
    c2lr = convert_2_lr(rows)
    return c2lr
  else:
    return 'ERROR! Incorrect d'

