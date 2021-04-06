
def numbers_to_ranges(lst):
  m=[]
  p=""
  f=[]
  if len(lst)==0:
    return []
  elif len(lst)==1:
    return [str(lst[0])]
  for l in range(len(lst)):
    if l==len(lst)-2:
      if lst[l]+1==lst[l+1]:
        m.append(lst[l])
        m.append(lst[l+1])
        p=str(min(m))+"-"+str(max(m))
        f.append(p)
        return f
      else:
        m.append(lst[l])
        if len(m)==1:
          p=str(m[0])
          f.append(p)
          p=""
        else:
          p=str(min(m))+"-"+str(max(m))
          f.append(p)
          p=""
        m.append(lst[l+1])
        p=str(m[0])
        f.append(p)
        return f
    if lst[l]+1==lst[l+1]:
      m.append(lst[l])
    else:
      m.append(lst[l])
      if len(m)==1:
        p=str(m[0])
        f.append(p)
        p=""
      else:
        p=str(min(m))+"-"+str(max(m))
        f.append(p)
        p=""
      m=[]

