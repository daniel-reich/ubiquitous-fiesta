
def max_product(lst):
  if len(lst)==3:
    return lst[0]*lst[1]*lst[2]
  l1=sorted([i for i in lst if i<0])
  l2=sorted([i for i in lst if i>=0],reverse=True)
  result=1
  if len(l1)<2:
    for i in l2[:3]:
      result*=i 
    return result
  elif l2==[]:
    for i in l1[-3:]:
      result*=i
    return result
  elif len(l2)<=2:
    return l2[0]*l1[0]*l1[1]
  else:
    if l1[0]*l1[1]*l2[0]>l2[0]*l2[1]*l2[2]:
      return l1[0]*l1[1]*l2[0]
    else:
      return l2[0]*l2[1]*l2[2]
​
def min_product(lst):
  l1=sorted([i for i in lst if i<0])
  l2=sorted([i for i in lst if i>=0],reverse=True)
  result=1
  if len(l1)==0:
    return l2[0]*l2[1]*l2[2]
  elif len(l1)<3:
    return l1[0]*l2[0]*l2[1]
  elif len(l2)<3:
    return l1[0]*l1[1]*l1[2]

