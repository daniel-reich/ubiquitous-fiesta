
def censor(s):
  z=s.split()
  lst=[x if len(x)<=4 else len(x)*'*' for x in z]
  return (' '.join(lst))

