
def accum(txt):
  return '-'.join([(l*i).capitalize() for i, l in enumerate(txt, 1)])

