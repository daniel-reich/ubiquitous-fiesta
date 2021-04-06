
import bisect
​
def probability(lst, n):
  lst.sort()
  fav = lst[bisect.bisect_left(lst,n):]
  return round(len(fav)/len(lst) * 100,1)

