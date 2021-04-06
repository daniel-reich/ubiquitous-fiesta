
def find_the_difference(s, t):
  for c in set(t):
    if s.count(c) != t.count(c):
      return c

