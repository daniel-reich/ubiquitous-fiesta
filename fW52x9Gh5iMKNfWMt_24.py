
def recaman_index(n):
  l = [0]
  while l[-1] != n:
    x = l[-1] - len(l)
    if x not in l and x > 0:
      l.append(x)
    else:
      l.append(l[-1] + len(l))
  return len(l) - 1

