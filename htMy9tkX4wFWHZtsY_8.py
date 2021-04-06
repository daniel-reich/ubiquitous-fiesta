
from datetime import datetime as dt
from datetime import timedelta as td
def palindrome_time(lst):
  t1 = dt(1,1,1,lst[0],lst[1],lst[2])
  t2 = dt(1,1,1,lst[3],lst[4],lst[5])
  count = 0
  while t1 <=t2:
    if str(t1.time())==str(t1.time())[::-1]:
      count+=1
    t1+= td(seconds=1)
  return count

