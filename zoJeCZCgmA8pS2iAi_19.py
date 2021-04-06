
def func_sort(lst):
  def calls(f, c=0):
    return calls(f(), c+1) if callable(f) else c
  return sorted(lst, key=calls)

