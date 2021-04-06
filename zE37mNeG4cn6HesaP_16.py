
def max_ham(s1, s2):
  count = 0
  if len(s1) != len(s2) or set(s1) != set(s2): return False
  for x, y in zip(s1, s2):
    if x != y: count += 1
  return True if count == len(s1) else count

