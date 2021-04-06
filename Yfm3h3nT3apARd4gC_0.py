
def rolls(l):
  return sum((0 if b==1 else 2*a if b==6 else a) for a,b in zip(l,[0]+l))

