
def func_sort(lst):
  return sorted(lst,key=func)
def func(x):
  count = 0
  while callable(x):
    count+=1
    x = x()
  return count

