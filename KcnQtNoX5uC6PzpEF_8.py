
def check_sum(lst, n):
  for i,x in enumerate(lst[:-1]):
    for y in lst[i+1:]:
      if x+y==n:
        return True
  return False

