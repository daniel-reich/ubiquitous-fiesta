
def stock_picker(lst):
  d=[]
  for i in range(len(lst)):
    for j in range ((i+1),len(lst)):
      d.append(lst[j]-lst[i])
  return max(d) if max(d)>=0 else -1

