
def max_ham(s1, s2):
  if set(s1) == set(s2):
    if sum(a == b for a, b in zip(s1, s2)) == 0:
      return True
    return len(s1) - sum(a == b for a, b in zip(s1, s2))
  return False

