
def balanced(lst):
  a = lst[:int(len(lst)/2)]
  b = lst[int(len(lst)/2):]
  
  if sum(a) == sum(b):
    return lst
  elif sum(a) > sum(b):
    return a+a
  else:
    return b+b

