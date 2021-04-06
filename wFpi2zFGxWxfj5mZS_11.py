
def count_true(lst):
  x=0
  
  for values in lst:
    if values==True:
      x= x+1
  
  if x:
    return x
  else:
    return 0

