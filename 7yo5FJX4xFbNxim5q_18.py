
def harry(p):
  x = 0
  y = 0
  if len(p[0]) < 1:
    return -1
  for i in range(len(p) - 1):
    x += p[i][0]
  for i in range(1, len(p)):
    y += p[i][-1]
  x += sum(p[-1])
  y += sum(p[0])
  return y if y > x else x

