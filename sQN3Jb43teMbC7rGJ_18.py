
def make_transpose(m):
  dm = len(m)
  dn = len(m[0])
  tm = [[0] * dm for i in range(dn)]
  for i in range(dm):
    for j in range(dn):
      tm[j][i] = m[i][j]
  return tm

