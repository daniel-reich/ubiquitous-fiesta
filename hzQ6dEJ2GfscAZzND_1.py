
def factory(n):
  def sub_factory(lst):
    return [i//n for i in lst]
  return sub_factory

