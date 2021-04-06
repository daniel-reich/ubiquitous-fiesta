
def can_put(txt, dim):
  res,curr = 0,0
  for lgw in [len(w) for w in txt.split()]:
    if lgw > dim[1]:
      return False
    if curr and curr + lgw + 1 <= dim[1]:
      curr +=  1 + lgw
    else:
      if curr:
        res += 1
      curr = lgw  
  if res >= dim[0]:
    return False
  return True

