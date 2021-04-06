
def is_ladder_safe(ldr):
  width = max(list(map(lambda x: x.count("#"),ldr)))
  if len(ldr[0]) < 5:
    return False
  elif width < 5:
    return False
  elif ldr[1].count("#") != width:
    return False
  else:
    indices = list(filter(lambda x: ldr[x].count("#") == width,range(0,len(ldr))))
    differences = list(map(lambda x: indices[x]-indices[x-1],range(1,len(indices))))
    if max(differences) > 3:
      return False
    else:
      return differences.count(differences[0]) == len(differences)

