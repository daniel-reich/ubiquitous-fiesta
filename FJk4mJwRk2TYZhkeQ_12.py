
def accum(txt):
  return '-'.join((char * (i + 1)).title() for i, char in enumerate(txt))

