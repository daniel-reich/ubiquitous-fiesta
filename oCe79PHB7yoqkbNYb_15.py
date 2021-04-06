
def break_point(num):
  lst = list(map(int,str(num)))
  
  l = len(lst)
  
  for i in range(1,l):
    if sum(lst[:i]) == sum(lst[i:]):
      return True
  return False

