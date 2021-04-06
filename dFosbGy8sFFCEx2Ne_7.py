
from bisect import *
​
def rank(lst):
  meh = sorted(lst)
  return [(bisect_left(meh,e)+bisect_right(meh,e)-1)/2 for e in lst]

