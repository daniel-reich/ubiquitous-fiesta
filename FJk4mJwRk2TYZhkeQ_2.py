
def accum(txt):
  return '-'.join(t.upper() + i*t.lower() for i, t in enumerate(txt))

