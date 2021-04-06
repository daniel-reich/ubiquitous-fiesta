
def can_put(txt, dim):
  leftx = dim[0]
  lefty = dim[1]
  for word in txt.split():
    if leftx == 0:
      return False
    if len(word) > dim[1]:
      return False
    if lefty == dim[1]:
      lefty -= len(word)
    else:
      lefty -= len(word) + 1
    if lefty == 0:
      leftx -= 1
      lefty = dim[1]
    elif lefty < 0:
      leftx -= 1
      lefty = len(word)
  return leftx > 0 or (leftx == 0 and lefty == dim[1])

