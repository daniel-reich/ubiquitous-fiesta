
def calculate_arrowhead(lst):
  p = 0 #position
​
  for i in ''.join(lst):
    if i == '<':
      p -= 1
​
    else:
      p += 1
  
  if p < 0:
    return '<' * abs(p)
  elif p > 0:
    return '>' * abs(p)
  else:
    return ''

