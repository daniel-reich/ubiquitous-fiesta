
def is_there_consecutive(lst, n, times):
  if times==0 and n not in lst:
    return True 
  x = 0
  for num in lst:
    if num == n:
      x += 1
      if x == times:
        return True
    else:
      x = 0
  return False

