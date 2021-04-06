
def replace(txt, r):
  rng = range(ord(r[0]),ord(r[-1])+1)
  return ''.join(['#' if ord(char) in rng else char for char in txt])

