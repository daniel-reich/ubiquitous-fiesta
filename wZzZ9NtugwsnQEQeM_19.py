
def golf_score(c, r):
  s = "eagle birdie par bogey double-bogey".split()
  return sum(a+s.index(b)-2 for a,b in zip(c,r))

