
from collections import Counter
def is_rectangle(n):
  c=list()
  if(len(Counter(n))!=4):
    return False  
  for i in n:
    i=i.replace(" ","")
    i=i.split(",")
    print(i)
    c.append([int(i[0][1:]),int(i[1][0:len(i[1])-1])])
​
  dis=list()
  for i in range(0,len(c)):
    for j in range(i+1,len(c)):
      dis.append(abs(c[j][1]-c[i][1])+abs(c[j][0]-c[i][0]))
  dis=Counter(dis)
  print(dis)
  if(len(dis)>3):
    return False
  else:
    return True

