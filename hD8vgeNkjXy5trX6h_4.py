
import itertools
def combo(lst, n):
  s = ''.join(map(str, lst))
  tup_lst = list(itertools.combinations(s,n))
  if s.isdigit():
    ll = [[int(x) for x in tup] for tup in tup_lst]
    return ll
  else:
    return [list(tup) for tup in tup_lst]

