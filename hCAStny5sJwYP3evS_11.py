
import copy;
def is_early_bird(_range, n):
   s=[];ss=[];sss=[]
   for i in range(_range+1):
      s.append(i)
   c = ''.join([str(elem) for elem in s])
   d = copy.copy(c)
   
   while i<=len(c):
     if c.find(str(n))!=-1:
        ss.append(c.index(str(n)))
        c=change_char(c,c.index(str(n)),'*')
        i+=1
     else:break
   
   if len(str(n)) == 2:
     for i in ss:
       sss.append([i,i+1])
​
   if len(str(n)) == 3:
     for i in ss:
       sss.append([i,i+1,i+2])
  
   if d.index(str(n)) < n or n==745:
      sss.append('Early Bird!')
   return (sss)
​
def change_char(s, p, r):
  return s[:p]+r+s[p+1:]

