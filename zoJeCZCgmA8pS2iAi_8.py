
def numCalls(fn):
  count = 0
  while callable(fn):
    fn = fn()
    count += 1
  return count
​
def func_sort(lst):
  return sorted(lst, key=numCalls)

