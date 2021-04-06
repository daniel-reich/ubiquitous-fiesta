
def factory(n):
  def first (a):
    result = []
    for i in a:
      result.append(i/n)
    return result
  return first

