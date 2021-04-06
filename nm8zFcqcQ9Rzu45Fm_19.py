
def bridge_shuffle(lst1, lst2):
  arr = []
  idx = 0
  
  for i in range(min(len(lst1),len(lst2))):
    arr.append(lst1[i])
    arr.append(lst2[i])
    idx = i
  
  if len(lst1)>len(lst2):
    for i in range(idx,len(lst1)-1):
      arr.append(lst1[i+1])
  elif len(lst1)<len(lst2):
    arr.append(lst2[i+1])
    
  return arr

