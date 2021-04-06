
import itertools
def combo(lst, n):
  a = list(itertools.combinations(lst, n))
  for i in range(len(a)):
    a[i] = list(a[i])
  return a

