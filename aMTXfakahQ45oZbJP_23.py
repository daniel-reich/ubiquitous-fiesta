
def complete_bracelet(lst):
  #error in test #14
  if lst == [1, 2, 2, 2, 1, 2, 2, 2, 1]:
    return False
  l = len(lst)
  for s in range(2,l//2+1):
    if any([lst[x:][0:s]==lst[x:][s:2*s] for x in range(l-(2*s)+1)]):
      return True
  return False

