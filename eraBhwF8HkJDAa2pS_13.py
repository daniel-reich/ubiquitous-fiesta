
def pirates_killed(g, t):
  return any(abs(a-max(g))>b for a,b in zip(g,t))

