
def generate_rug(n, direction):
  m = list(range(n))
  if direction == 'left':
    rug = [m]
    for i in range(1, n):
      new = [i] + rug[-1][:-1]
      rug.append(new)
  else:
    m.reverse()
    rug = [m]
    for i in range(1, n):
      new = rug[-1][1:] + [i]
      rug.append(new)
  return rug

