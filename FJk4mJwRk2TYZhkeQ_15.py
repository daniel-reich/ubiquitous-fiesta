
def accum(txt):
  return '-'.join((v*(i+1)).capitalize() for i,v in enumerate(txt))

