
def find_the_difference(s, t):
  for i in t:
    if s.count(i)!=t.count(i):
      return i

