
def return_unique(lst):
  arr=[]
  for l in lst:
    if lst.count(l)==1:
      arr.append(l)
  return arr

