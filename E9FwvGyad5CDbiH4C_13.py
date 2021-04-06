
def block(l):
  b = 0
  for i, x in enumerate(l):
    for j in x:
      if j == 2:
        b += len(l)-i-1
  return b

