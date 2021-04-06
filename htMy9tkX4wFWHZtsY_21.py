
from datetime import datetime,timedelta
def palindrome_time(lst):
  a,b,c,x,y,z = [str(i) for i in lst]
  palin = []
  start = datetime.strptime(a+':'+b+':'+c,'%H:%M:%S')
  end = datetime.strptime(x+':'+y+':'+z,'%H:%M:%S')
  while start<=end:
    temp=start.strftime("%H:%M:%S")
    if is_pal(temp):
      palin.append(temp)
    start+=timedelta(seconds=1)
  return len(palin)
  
def is_pal(s):
  return s==s[::-1]

