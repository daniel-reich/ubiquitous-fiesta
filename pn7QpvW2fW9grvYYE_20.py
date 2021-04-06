
def find_fulcrum(lst):
  x=1
  while x < len(lst):
    left=[]
    right=[]
    temp=0
    while temp<x:
      left.append(lst[temp])
      temp+=1
    temp=x+1
    while temp<len(lst):
      right.append(lst[temp])
      temp+=1
    if sum(left)==sum(right):
      return lst[x]
    x+=1
    left
  return -1

