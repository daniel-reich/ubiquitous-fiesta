
def change_types(lst):
  s=[]
  for x in lst:
    if type(x)==str:
      s.append(x[0].upper()+x[1:]+"!")
    elif x%2==0:
      s.append(x+1)
    elif type(x)==bool:
      s.append(not x)
    else:
      s.append(x)
  return s

