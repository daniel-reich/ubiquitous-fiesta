
def find_the_difference(s, t):
  for x in set(s+t):
    if s.count(x)!=t.count(x):
      return x

