
def reversible_inclusive_list(f, t):
  return list(range(f, t+1, 1) if f<t else range(f, t-1, -1))

