
def upward_trend(lst):
  true = 0
  t = 0
  re = True
  for a in lst:
    if isinstance(a,str):
      re = False
      t = 1
  if re:
    for a in range(len(lst)-1):
      if lst[a] < lst[a+1]:
        true = true + 1
      else:
        true = 0
  if true == len(lst) - 1 and re:
    return True
  elif t == 1:
    return "Strings not permitted!"
  else:
    return False

