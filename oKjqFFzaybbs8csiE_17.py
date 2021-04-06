
def cons(lst):
  min = sorted(lst)[0]
  max = sorted(lst)[-1]
  lst2 = []
  for i in range(min, max+1):
    lst2.append(i)
  if sorted(lst) == lst2:
    return True 
  return False

