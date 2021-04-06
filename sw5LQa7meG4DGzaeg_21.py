
def multiply(lst):
  def multipl(i):
    return [item*i for item in lst]
  return multipl

