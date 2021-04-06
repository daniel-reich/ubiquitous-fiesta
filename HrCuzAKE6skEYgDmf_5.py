
def pairs(lst):
  if len(lst) % 2 != 0: 
    mid = int(len(lst)/2)
    lstOne = [[lst[i], lst[len(lst)-i-1]] for i in range(0, mid+1)]
    return lstOne
  else: 
    mid = int((len(lst))/2) - 1
    lstOne = [[lst[i], lst[len(lst)-i-1]] for i in range(0, mid+1)]
    return lstOne

