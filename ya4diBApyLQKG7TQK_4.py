
def validate_relationships(txt):
  str1=""
  st2=""
  ls=[]
  k=[]
  res1=[]
  res2=[]
  flag=True
  for i in txt:
    if i in ['0','1','2','3','4','5','6','7','8','9','-']:
      k.append(st2)
      st2=""
      str1+=i
    else:
      st2+=i
      ls.append(str1)
      str1=""
  ls.append(str1)
  for i in ls:
    if not i=='':
      res1.append(int(i))
  for i in k:
    if not i=='':
      res2.append(i)
  for i in res2:
    if i=='=':
      if res1[0]!=res1[1]:
        flag=False
        break
      else:
        res1=res1[1:]
    elif i=='<=':
      if res1[0]>res1[1]:
        flag=False
        break
      else:
        res1=res1[1:]
    elif i=='>=':
      if res1[0]<res1[1]:
        flag=False
        break
      else:
        res1=res1[1:]
    elif i=='<':
      if res1[0]>=res1[1]:
        flag=False
        break
      else:
        res1=res1[1:]
    elif i=='>':
      if res1[0]<=res1[1]:
        flag=False
        break
      else:
        res1=res1[1:]
  return flag

