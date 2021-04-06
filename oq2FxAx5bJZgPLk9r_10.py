
import collections
def sock_merchant(lst):
  D=collections.Counter(lst)
  return sum(int(D[x]//2) for x in D)

