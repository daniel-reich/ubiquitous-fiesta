
def func_sort(lst):
  def count_calls(f):
    cnt = 0
    while(callable(f)):
      f = f()
      cnt += 1
    return cnt
  return sorted(lst, key=count_calls)

