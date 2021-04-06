
def can_put(txt, dim):
  if len(txt) <= dim[0] * dim[1]:
    if all(True if len(i) <= dim[1] else False for i in txt.split()):
      return True
  return False

