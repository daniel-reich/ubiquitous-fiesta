
def find_the_difference(s, t):
  return [i for i in t if t.count(i)!=s.count(i)][0]

