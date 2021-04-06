
def cons(lst):
  lst.sort()
  for i in range(len(lst)-1):
    if lst[i] != lst[i+1] - 1:
      return False
  return True

