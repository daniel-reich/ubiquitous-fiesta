
def can_put(txt, dim):
  a = txt.split()
  return False if len(max(a, key=len)) > dim[1] or len(txt) > dim[0] * dim[1] else True

