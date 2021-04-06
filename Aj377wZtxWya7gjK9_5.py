
def sum_missing_numbers(lst):
  total = 0
  a = min(lst)
  print(a)
  b = max(lst)
  print(b)
  for i in range(a,b+1):
    if i not in lst:
      total+=i
  return total

