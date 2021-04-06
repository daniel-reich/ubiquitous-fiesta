
def shared_digits(lst):
  lst = list( map( set, map(str,lst) ) )
  for i in range(len(lst)-1):
    if lst[i].intersection(lst[i+1]) == set(): return False
  return True

