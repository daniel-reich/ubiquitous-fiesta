
def factory(n):
  def func(lst):
    return [i/n for i in lst]
  return func

