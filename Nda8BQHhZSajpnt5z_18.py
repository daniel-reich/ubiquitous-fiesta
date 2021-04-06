
def GCD(lst):
  x=[]
  for items in range(1,lst[0]+1):
    if lst[0]%items==0:
      x.append(items)
  
  x.sort()
  x.reverse()
  y=[]
  for items in x:
    c=[]
    for item in lst:
      if item%items==0:
        c.append(True)
      else:
        c.append(False)
    if c.count(False)==0:
      y.append(items)
  
    
  if len(y)==0:
    return 1
  else:
    return max(y)

