
def drange(*args):
  i, res = 0, []
  if len(args) == 1:
    return tuple(i for i in range(args[0]))
  elif len(args) == 2:
    return tuple(i for i in range(args[0], args[1]))
  i = args[0]
  while i < args[1]:
    res.append(round(i, 3))
    i += args[2]
  return tuple(res)

