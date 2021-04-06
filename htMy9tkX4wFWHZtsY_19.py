
from datetime import datetime,timedelta
def palindrome_time(lst):
   a=[];k=0
   s1 = str(lst[0]) + ':' + str(lst[1]) +':' + str(lst[2])
   s2 = str(lst[3]) + ':' + str(lst[4]) + ':' + str(lst[5])
   FMT = '%H:%M:%S'
   t1 = datetime.strptime(s1, FMT)
   t2 =  datetime.strptime(s2, FMT)
   while t1<=t2:
     a.append(str(t1)[11:13]+str(t1)[14:16]+str(t1)[17:19])
     t1 = t1 + timedelta(0, 1)
   for i in a:
       if i==i[:-9:-1]:
          k=k+1
   return (k)

