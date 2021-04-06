
def can_traverse(x):
  return all(abs(sum(i)-sum(j))<2 for i,j in zip(zip(*x),list(zip(*x))[1:]))

