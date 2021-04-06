
def sum_missing_numbers(lst):
  a=min(lst)
  b=max(lst)
  s = 0
  for i in range(a,b+1):
    if(i not in lst):
      s += i
  return s

