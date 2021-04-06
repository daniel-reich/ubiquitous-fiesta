
def pairwise_swap(list_of_elements):
  
  odd_flag=0
  lim = len(list_of_elements)
  if lim%2!=0:
    odd_flag=1
  
  if odd_flag==0:
    i = 0
    while i<lim:
      list_of_elements[i],list_of_elements[i+1]=list_of_elements[i+1],list_of_elements[i]
      i+=2
    return list_of_elements
  
  eq_flag=0
  mx = 0
  idx = -1
  i = 0
  while i<lim-1:
    t = 0
    for j in range(0,len(str(list_of_elements[i]))):
      t+=ord(str(list_of_elements[i])[j])
    
    if t>mx:
      mx = t
      idx = list_of_elements[i]
    elif t==mx:
      eq_flag=1
    t = 0
    for j in range(0,len(str(list_of_elements[i+1]))):
      t+=ord(str(list_of_elements[i+1])[j])
    
    if t>mx:
      mx = t
      idx = list_of_elements[i+1]
    elif t==mx:
      eq_flag=1
    list_of_elements[i],list_of_elements[i+1]=list_of_elements[i+1],list_of_elements[i]
    i+=2
    
  t = 0
  for j in range(0,len(str(list_of_elements[-1]))):
    t+=ord(str(list_of_elements[-1])[j])
    
  if t>mx:
    mx = t
    idx = list_of_elements[-1]
    eq_flag=0
  elif t==mx:
    eq_flag=1
    
    
  idx = list_of_elements.index(idx)
  print(eq_flag)
  if eq_flag==1:list_of_elements[0],list_of_elements[-1]=list_of_elements[-1],list_of_elements[0]
  else:list_of_elements[idx],list_of_elements[-1]=list_of_elements[-1],list_of_elements[idx]
  
  return list_of_elements

