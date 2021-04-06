
def accum(txt):
  return '-'.join(c.upper() + c.lower()*i for (i, c) in enumerate(txt))

