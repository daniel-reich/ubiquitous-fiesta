
def accum(txt):
  return '-'.join([ch.upper()+(i*ch.lower()) for i, ch in enumerate(txt)])

