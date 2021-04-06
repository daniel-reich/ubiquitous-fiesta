
def check(lst):
  m=lst.index(min(lst))
  L=sorted(lst)
  if L==lst:
    return 'NO'
  else:
    return 'YES' if lst[m:]+lst[:m]==L else 'NO'

