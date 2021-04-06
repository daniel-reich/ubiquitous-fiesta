
def func_sort(lst):
  return sorted(lst, key=calls_for_non_func)
  
def calls_for_non_func(x):
  calls = 0
  while True:
    try:
      x = x()
      calls += 1
    except TypeError:
      return calls

