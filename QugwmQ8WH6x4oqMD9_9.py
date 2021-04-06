
import itertools
​
def count_identical_lists(lst1, lst2, lst3, lst4):
  cnt=0
  for x,y in itertools.combinations([lst1,lst2,lst3,lst4],2):
    if x==y: cnt+=1
  if not cnt: return 0
  for i in range(1,5):
    if sum(range(i+1))==cnt:
      return i+1

