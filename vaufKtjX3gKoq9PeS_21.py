
def ohms_law(v, r, i):
  ls=[]
  count = 0
  ls.append(v)
  ls.append(r)
  ls.append(i)
  for n in ls:
    if n == None:
      count+=1
  if count==0 or count >1:
    return "Invalid"
  else:
    if ls[0] == None:
      return round(ls[1]*ls[2],2)
    elif ls[1] == None:
      return round(ls[0]/ls[2],2)
    else:
      return round(ls[0]/ls[1],2)

