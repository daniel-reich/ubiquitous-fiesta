
def accumulating_list(lst):
  x=[]
  y=0
  for i in range(len(lst)):
    y+=lst[i]
    x.append(y)
  return x

