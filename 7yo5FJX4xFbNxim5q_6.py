
def harry(po):
  if not po[0]:
    return -1
  n = len(po)-1
  m = len(po[0])-1
  if not (n or m):
    return po[0][0]
  elif not n:
    return po[n][m] + harry([i[:-1] for i in po])
  elif not m:
    return po[n][m] + harry(po[:-1])
  else:
    return po[n][m] + max(harry(po[:-1]), harry([i[:-1] for i in po]))

