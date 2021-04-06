
def dance(lst,parameter):
  w=[]
  m=[]
  for i in range(len(lst)):
    w.append(lst[i][0])
    m.append(lst[i][1])
  if parameter=='men':
    m=m[::-1]
    return [[w[i],m[i]] for i in range(len(lst))]
  if parameter=='women':
    w=w[::-1]
    return [[w[i],m[i]] for i in range(len(lst))]

