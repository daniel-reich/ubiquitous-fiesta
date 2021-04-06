
def max_ham(s1, s2):
  c = 0
  for a, b in zip(s1,s2):
    c += (a != b)
  return False if sorted(s1) != sorted(s2) else (True if c == len(s1)  else c)

