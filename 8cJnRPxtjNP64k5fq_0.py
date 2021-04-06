
def dance(lst,par):
  (i,j) = (1,-1) if par == "men" else (-1,1) 
  return [[a[0],b[1]] for a,b in zip(lst[::i],lst[::j])]

