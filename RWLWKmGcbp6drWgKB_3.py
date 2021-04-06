
def chosen_wine(wines):
  if not wines:
    return None
  else:
    lstv=[]
    cnt=0
    for i in wines:
      if type(i)==dict:
        cnt+=1
    if cnt==1:
      lstvv=[]
      for i in wines:
        for k,v in i.items():
          lstvv.append(v)
      return lstvv[0]
    else:
      for i in wines:
        for k,v in i.items():
          lstv.append(v)
      ll=lstv.copy()
      for i in lstv:
        if type(i)==str:
          lstv.remove(i)
      lstv.sort()
      return ll[ll.index(lstv[1])-1]

