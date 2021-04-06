
def find_difference(a, b):
  def prod(lst):
    x=1
    for i in lst:
      x*=i
    return x
  return abs(prod(a)-prod(b))

