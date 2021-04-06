
def find_the_difference(s,t):
  t=sorted(t)
  for x,y in zip(sorted(s),t[:-1]):
    if x!=y:return y
  return t[-1]

