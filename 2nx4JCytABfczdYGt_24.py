
def conjugate(v, p):
  pronouns = [
  ('Io','o'), ('Tu','i'), ('Egli', 'a'), 
  ('Noi','iamo'), ('Voi','ate'), ('Essi','amo')
  ]
  
  pronoun, ending = pronouns[p-1][0], pronouns[p-1][1] 
  root = v[:-3]
  if root[-1] in 'cg':
    root += 'h'
  elif root[-1] == 'i':
    ending = ending.replace('i','')
    
  return '{} {}{}'.format(pronoun, root, ending)

