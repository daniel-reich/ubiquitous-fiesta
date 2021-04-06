
def is_parallelogram(lst):
  l = sorted(lst)
  return all(l[0][i]+l[3][i]==l[1][i]+l[2][i] for i in [0,1])

