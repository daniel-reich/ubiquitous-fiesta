
def swap_dict(dic):
  res={}
  items=[(x,[y]) for y,x in dic.items()]
  for x in items:
    if x[0] not in res:res[x[0]]=x[1]
    else:res[x[0]].append(x[1][0])
  return res

