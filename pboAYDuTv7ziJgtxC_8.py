
def min_turns(c, t):
  return sum([min([abs(int(c[i]) - int(t[i])), 10- abs(int(c[i]) - int(t[i]))]) for i in range(4)])

