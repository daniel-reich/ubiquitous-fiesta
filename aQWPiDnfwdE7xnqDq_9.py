
def drange(*args):
  myans = []
  if len(args) == 3:
    a = args[0]
    while a < args[1]:
      myans.append(round(a,3))
      a += args[2]
    return tuple(myans)
  elif len(args) == 2:
    a = args[0]
    while a < args[1]:
      myans.append(round(a,3))
      a += 1
    return tuple(myans)
  else:
    for i in range(args[0]):
      myans.append(i)
    return tuple(myans)

