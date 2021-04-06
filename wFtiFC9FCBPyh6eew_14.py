
def partitions(n):
  l,main=[2],[]
  l3=[]
  for i in range(n-1):
    l2=[[1 for x in range(n-l[-1])]]
    l2[0].append(l[-1])
    for x in range(n):
      if len(l2)!=0:l3.append(l2)
      for i in l2:
        for j in l:
          if i.count(1)>=j:
            i.append(j)
            main.append(i[j::])
            i.remove(j)
      l2=[x for x in main]
      main=[]
    l.append(l[-1]+1)
  l4=[]
  for x in range(len(l3)):
    for y in range(len(l3[x])):
      l3[x][y].sort()
      if l3[x][y] not in l4 : l4.append(l3[x][y])
  return len(l4)+1
print(partitions(19))

