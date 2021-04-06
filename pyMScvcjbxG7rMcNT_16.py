
def sum_list(lst):
  s = 0
  for i in lst:
    if isinstance(i,list):
      s+=sum_list(i)
    else:
      s+=i
  return s

