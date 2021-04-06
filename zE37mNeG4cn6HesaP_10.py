
def max_ham(s1, s2):
  if set(s1) == set(s2):
    res = sum(x!=y for x, y in zip(s1, s2))
    return res == len(s1) or res
  return False

