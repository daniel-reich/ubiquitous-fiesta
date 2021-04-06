
def func_sort(lst):
  def nb_calls(func):
    ans = 0
    while callable(func):
      func = func()
      ans += 1
    return ans
  return sorted(lst, key = nb_calls)

