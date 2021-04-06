
def factory(n):
  def list_multiplication(lst):
    return [el / n for el in lst]
  return list_multiplication

