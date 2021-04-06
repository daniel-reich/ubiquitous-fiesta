
def cons(lst):
  lst.sort()
  for i in range(1,len(lst)):
    if lst[i] - lst[i - 1] != 1:
      return False
  return True

