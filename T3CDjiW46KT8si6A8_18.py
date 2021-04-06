
def product(lst):
  lst=list(set(lst))
  ma=max(lst)
  if len(lst)>1:
    lst.remove(ma)
  return ma*max(lst)

