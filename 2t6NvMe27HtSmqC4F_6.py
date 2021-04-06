
def boolean_and(lst):
  while len(lst)>1:
    lst[0:2]=[lst[0] and lst[1]]
  return lst[0]
​
​
def boolean_or(lst):
  while len(lst)>1:
    lst[0:2]=[lst[0] or lst[1]]
  return lst[0]
  
​
def boolean_xor(lst):
  while len(lst)>1:
    lst[0:2]=[lst[0]!=lst[1]]
  return lst[0]

