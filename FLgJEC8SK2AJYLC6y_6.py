
def possible_path(lst):
  for cur,fut in zip(lst,lst[1:]):
    if cur=='H' and fut in (1,3) or cur in (1,3) and fut=='H':
      return False
    if isinstance(cur,int) and isinstance(fut,int) and cur%2==fut%2:
      return False
  return True

