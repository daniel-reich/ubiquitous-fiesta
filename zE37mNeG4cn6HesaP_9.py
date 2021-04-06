
def max_ham(s1, s2):
  a = sum([1 for x, y in zip(s1, s2) if x!=y])
  if sorted(s1) != sorted(s2):
    return False
  else:
    if a == len(s1):
      return True
    return a

