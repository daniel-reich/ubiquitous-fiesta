
def factory(n):
  def split_n(lst):
    return [i /n for i in lst]
  return split_n

