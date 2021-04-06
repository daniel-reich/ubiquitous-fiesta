
def nameShuffle(name):
  a, b = name.split()
  a, b = b, a
  return ' '.join((a, b))

