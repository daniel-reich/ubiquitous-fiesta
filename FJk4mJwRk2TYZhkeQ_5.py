
def accum(txt):
  return '-'.join((s*(i+1)).title() for i, s in enumerate(txt))

