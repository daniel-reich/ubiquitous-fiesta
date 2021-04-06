
def palindrome_time(lst):
 start=(["0"+str(i) if len(str(i))==1 else str(i) for i in lst[:3]])
 end=(["0"+str(i) if len(str(i))==1 else str(i) for i in lst[3:]])
 count=0
 for h in range(int(start[0]),int(end[0])+1):
  for m in range(00,60):
   for s in range(00,60):
     x="".join(str("%.2d"%h)+str("%.2d"%m)+str("%.2d"%s))
     if int("".join(start))<=int(x)<=int("".join(end)) and  x==x[::-1]:
      count+=1
​
 return count

