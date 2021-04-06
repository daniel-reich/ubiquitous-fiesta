
def change_types(lst):
  res = []
  for i in range(len(lst)):
    elt = lst[i]
    if isinstance(elt,int) and not isinstance(elt,bool):
      if elt%2==0: elt+=1
      res.append(elt)
    elif isinstance(elt,str):
      res.append(elt.capitalize()+"!")
    else:
      res.append(not elt)
  return res

