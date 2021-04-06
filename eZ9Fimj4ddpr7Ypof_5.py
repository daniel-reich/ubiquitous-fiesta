
def mumbling(s):
  return '-'.join([(x+x*v).capitalize() for v,x in enumerate(list(s.lower()))])

