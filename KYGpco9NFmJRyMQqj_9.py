
def min_removals(txt1, txt2):
  s1 = set(txt1)
  s2 = set(txt2)
  l1 = len(s1.difference(s2))
  l2 = len(s2.difference(s1))
  return l1+l2

