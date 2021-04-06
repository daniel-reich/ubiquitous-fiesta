
def replace_next_largest(lst):
  x=sorted(lst)
  for i in range(len(lst)):
    num=lst[i]
    del lst[i]
    if num==x[-1]:
      lst.insert(i,-1)
    else:
      lst.insert(i,x[x.index(num)+1])
  return lst

