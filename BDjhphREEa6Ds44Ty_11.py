
def bomb(lst):
  for i in lst:
    if i[2]==0:return (i[0],i[1])
  lst.sort(key=lambda x:-x[2])
  lst=[lst[i][:2]+[lst[i][2]/lst[0][2]] for i in range(len(lst))]
  eq='abs((({}-x)**2+({}-y)**2)/(({}-x)**2+({}-y)**2)-{}**2)'
  dif=1
  for x in range(51):
    for y in range(51):
      try:
        a = eval(eq.format(lst[1][0],lst[1][1],lst[0][0],lst[0][1],lst[1][2]))
        b = eval(eq.format(lst[2][0],lst[2][1],lst[0][0],lst[0][1],lst[2][2]))
        if a+b<dif:dif=a+b;mem=(x,y)
      except:pass
  return mem

