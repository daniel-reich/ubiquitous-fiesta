
def list_less_than_100(lst):
  sum = 0
  
  for i in lst:
    sum += i
  if sum < 100:
    return True
  else:
    return False

