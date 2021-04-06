
def is_correct_aliases(names, aliases):
  f = lambda x,y: x[0]==y.split(' ')[0][0] and x[0]==y.split(' ')[1][0]
  return all([f(n,a) for n,a in zip(names, aliases)])

