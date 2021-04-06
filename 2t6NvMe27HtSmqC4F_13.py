
def boolean_and(lst):
  j=lst[0]
  for i in lst[1:]:
    j=j and i
  return(j) 
  
​
def boolean_or(lst):
  j=lst[0]
  for i in lst[1:]:
    j=j or i
  return(j) 
  
​
  
​
def boolean_xor(lst):
  j=lst[0]
  for i in lst[1:]:
    j=j ^ i
  return(j)

