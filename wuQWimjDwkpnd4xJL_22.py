
def balanced(lst):
  l = lst[:len(lst)//2]
  r = lst[len(lst)//2:]
  if sum(l) > sum(r):
    return l+l
  elif sum(l) < sum(r):
    return r + r
  else:
    return lst

