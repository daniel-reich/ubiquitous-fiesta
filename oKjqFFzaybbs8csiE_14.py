
def cons(lst):
  lst = sorted(lst)
  for i in range(len(lst)-1):
    #if lst[i] == lst[i+1]:
    # return False
    if lst[i+1]-lst[i] != 1:
      return False
  return True

