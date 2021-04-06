
def build_staircase(height, block):
  if height == 0:
    return []
  a = list()
  b = list()
  for x in range(height):
    y = x
    for y in range(x + 1):
      a.append(block)
    for z in range(height- y - 1):
      a.append("_")
    b.append(a)
    a = []
  return b

