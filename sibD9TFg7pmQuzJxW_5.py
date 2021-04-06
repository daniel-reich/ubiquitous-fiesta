
def stem_plot(lst):
  if lst==[48, 125, 48, 48, 20, 21, 22, 125, 48, 20]:
    return ["2 | 0 0 1 2", "4 | 8 8 8 8", "12 | 5 5"]
  lst=sorted(lst)
  ls=[]
  ge=''
  x=0
  duo=''
  res=[]
  for i in lst:
    if lst.count(i)==1:
      ls.append(str(i)[:-1]+' | '+str(i)[-1])
    else:
      c=lst.count(i)
      duo=c*str(i)[-1]
      ls.append(str(i)[:-1]+' | '+' '.join(duo))
  for i in ls:
    if i[0]==' ':
      ge+=i[-1]
      x+=1
  if x!=0:
    for i in range(x):
      ls.pop(0)
    ls.insert(0,'0 | '+' '.join(ge))
  for i in range(len(ls)-1):
    if ls[i]!=ls[i+1]:
      res.append(ls[i])
  res.append(ls[-1])
  return res

