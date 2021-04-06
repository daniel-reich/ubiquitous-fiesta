
import itertools
def combo(lst, n):
  mylist = []
  for comb in itertools.combinations(lst, n):
    mylist.append(list(comb))
  return mylist

