
def calculate_arrowhead(lst):
  r = 0
  l = 0
  for i in lst:
    r += i.count('>')
    l += i.count('<')
  if r > l:
    r = r-l
    return '>'*r
  elif l > r:
    l = l-r
    return '<'*l
  else:
    return ''

