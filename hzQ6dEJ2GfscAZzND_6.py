
def factory(n):
  def divide_by_15(lst):
    return [i/n for i in lst]
  return divide_by_15

