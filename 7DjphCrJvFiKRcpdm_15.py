
def covered_integers(lst):
  l = []
  for i in lst:
    l += [j for j in range(i[0], i[1] + 1)]
  return len(set(l))

