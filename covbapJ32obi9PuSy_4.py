
def diamond_arrays(x):
  l = [[i + 1 for x in range(i + 1)] for i in range(x)]
  return l + l[-2::-1] if len(l) > 1 else l

