
def factory(n):
  def newFunc(l):
    return [x/n for x in l]
  return newFunc

