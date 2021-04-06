
def sort_by_string(lst, txt):
  x=[]
  for i in txt:
    for j in lst:
      if j[0]==i:
        x.append(j)
  return x

