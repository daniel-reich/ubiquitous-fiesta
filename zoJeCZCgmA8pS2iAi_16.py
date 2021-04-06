
def func_sort(lst):
  return sorted(lst, key=calls)
  
def calls(i):
  result = 0
  while callable(i):
    result += 1
    i = i()
  return result

