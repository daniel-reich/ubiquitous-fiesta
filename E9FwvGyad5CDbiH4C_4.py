
def block(lst):
  x = 0
  y = len(lst[0])
  for a in range(y):
    for b in range(len(lst) - 1):
      if lst[b][a] > lst[b + 1][a]:
        x += len(lst) - 1 - b
        break
  return x

