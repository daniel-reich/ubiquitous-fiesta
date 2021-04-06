
def multiply(lst):
  def mult(x):
    return [n*x for n in lst]
  return mult

