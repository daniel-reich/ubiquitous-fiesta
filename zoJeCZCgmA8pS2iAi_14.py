
def func_sort(lst):
  func_type = type(func_sort)
  def call_count(f):
    if type(f) != func_type:
      return 0
    return call_count(f()) + 1
  return sorted(lst, key = lambda f: call_count(f))

