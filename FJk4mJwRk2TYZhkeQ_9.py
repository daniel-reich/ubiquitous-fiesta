
def accum(txt):
  return '-'.join(x.upper() + x.lower()* y for (y, x) in enumerate(txt))

