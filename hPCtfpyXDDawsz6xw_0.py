
def verbify(txt):
  first, last = txt.split()
  
  if first.endswith('e'):
    first += 'd'
    
  elif not first.endswith('ed'):
    first += 'ed'
    
  return '{} {}'.format(first, last)

