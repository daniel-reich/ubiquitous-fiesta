
def find_the_difference(s, t):
  return "".join(set(i for i in t if t.count(i) > s.count(i) ))

