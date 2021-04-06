
def stock_picker(lst):
  big=lst[1]-lst[0]
  for i in range(len(lst)):
    for j in range(i+1,len(lst)):
      if lst[j]-lst[i]>big: big=lst[j]-lst[i]
  return big if big>0 else -1

