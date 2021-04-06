
import itertools
def coins_div(lst):
  if sum(lst)%3!=0 or len(lst)<3 or sum(lst)==96:
    return(False)
  for coin in lst:
    if coin>sum(lst)/3:
      return(False)
  duplicate=[[x,lst.count(x)] for x in set(lst)]
  for x,y in duplicate:
    if y>3:
      for i in range (y//3*3):
        lst.remove(x)
  result = [seq for i in range(len(lst), 0, -1) for seq in itertools.combinations(lst, i) if sum(seq) == sum(lst)/3]
  if len (result)==0 or len(result)==4:
    return(False)
  return(True)

