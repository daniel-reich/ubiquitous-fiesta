
def can_traverse(x):
  y=[i.count(1) for i in zip(*x)]
  return all([y[i+1] in range(y[i]-1,y[i]+2) for i in range(len(y)-1)])

