
def left_side(lst):
  res = [0]
  for x in range(1,len(lst)):
    count =0
    for y in range(x):    
      if lst[x]> lst[y]:
        count+=1
    res.append(count)
  return res
  
def right_side(lst):
  res = []
  for x in range(len(lst)):
    count=0
    for y in range(x, len(lst)):
      if lst[x]> lst[y]:
        count+=1
    res.append(count)
  return res

