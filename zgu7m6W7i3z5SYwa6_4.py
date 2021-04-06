
def sum(str):
  sum=0
  for i in str:
    sum+=int(i)
  return sum
  
def is_equal(lst):
  if(len(lst)==2):
    return sum(str(lst[0]))==sum(str(lst[1]))

