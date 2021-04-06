
def simple_pair(lst, n):
  for i in range(len(lst)):
    #lst2 = lst[i+1:]
    for j in lst[i+1:]:
      first = lst[i]
      second = j
      if check_multiply(first,second,n) == 1:
        return [first,second]
  return None
  
  
def check_multiply(x,y,n):
  if x*y == n:
    return 1
  else:
    return 0

