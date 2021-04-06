
def factory(n):
  def divider(lst=[]):
    return [i / n for i in lst]
  return divider

