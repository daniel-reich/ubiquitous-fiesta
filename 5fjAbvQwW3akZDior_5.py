
def unrepeated(txt):
  return ''.join(x for i, x in enumerate(txt[::-1]) if x not in txt[::-1][i+1:])[::-1]

