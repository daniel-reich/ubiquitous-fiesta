
def verbify(txt):
  a = txt.split()
  if a[0][-1] == 'e':
    a[0] = a[0] +'d'
  elif a[0][-2::] != 'ed':
    a[0] = a[0] + 'ed'
    
  return(' '.join(a))

