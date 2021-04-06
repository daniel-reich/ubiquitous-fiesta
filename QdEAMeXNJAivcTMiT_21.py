
def boxes(weights):
  newlst=[]
  lst=[]
  w_count=0
  for i in weights:
    if w_count+i<11:
      lst.append(i)
      w_count+=i
    else:
      newlst.append(lst)
      lst=[i]
      w_count=i
  newlst.append(lst)
  return len(newlst)

