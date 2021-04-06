
def can_play(x, w):
  y = sum([i.split() for i in x], [])
  z = w.split()[0] in y or w.split()[-1] in y
  return z

