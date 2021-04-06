
def counter(f):
  return 1 if not callable(f) else 1 + counter(f())
​
def func_sort(lst):
  return sorted(lst, key=counter)

