
from datetime import datetime, timedelta
def palindrome_time(lst):
  t1=datetime(2020,11,1,lst[0], lst[1], lst[2])
  t2=datetime(2020,11,1,lst[3], lst[4], lst[5])
  td=timedelta(seconds=1)
  if t1==t2:
    if datetime.strftime(t1,'%H:%M:%S')==datetime.strftime(t1,'%H:%M:%S')[::-1]:
      return 1
    else:
      return 0
  else:
    c=0
    while t1!=t2:
      if datetime.strftime(t1,'%H:%M:%S')==datetime.strftime(t1,'%H:%M:%S')[::-1]:
        c+=1
      t1+=td  
    if datetime.strftime(t2,'%H:%M:%S')==datetime.strftime(t2,'%H:%M:%S')[::-1]:
      c+=1
    return c

