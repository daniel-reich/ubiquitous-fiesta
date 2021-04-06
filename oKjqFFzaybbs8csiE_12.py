
def cons(lst):
  mylist = []
  lst = sorted(lst)
  for i in range (len(lst)-1):
    if not (lst[i]+1==lst[i+1]):
      return False
  return True

