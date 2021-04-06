
def func(lst):
  if isinstance(lst, list):
    return len(lst) + sum( [ func(ele) for ele in lst ] )
  else:
    return 0

