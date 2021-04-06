
def bar_chart(n):
  x=''
  val=list()
  val.extend(n.values())
  val.sort(reverse=True)
  key=list()
  key.extend(n.keys())
  key.sort()
  l=list()
  for i in val:
    for j in key:
      if(n[j]==i and j not in l):
        l.append(j)
        break   
  print(l)
  for i in l:
    if(n[i]!=0):
      z="#"*(n[i]//50)
      x+=i+"|"+z
      x+=" "+str(n[i])+"\n"
    else:
      x+=i+"|0\n"
​
  return x[0:len(x)-1]

