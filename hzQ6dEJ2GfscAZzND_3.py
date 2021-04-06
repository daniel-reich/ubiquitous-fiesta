
def factory(n):
  def inside(lst):
    return [i//n for i in lst]
  return inside

