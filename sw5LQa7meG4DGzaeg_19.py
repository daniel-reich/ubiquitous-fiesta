
def multiply(lst):
  def multiply_list(x):
    return [el * x for el in lst]
  return multiply_list

