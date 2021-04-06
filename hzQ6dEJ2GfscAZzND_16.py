
def factory(n):
  def lst(y):
    return [i//n for i in y]
  return lst

