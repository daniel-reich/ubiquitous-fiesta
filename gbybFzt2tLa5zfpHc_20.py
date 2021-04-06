
import itertools
def three_sum(lst):
  k = [x for x in itertools.combinations(lst,3)]
  res = []
  for i in k:
    temp = [x for x in i]
    if sum(temp)==0 and temp not in res:
      res += [temp]
      
      
  return res

