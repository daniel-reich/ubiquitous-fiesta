
def factory(n):
  def div_lst(lst):
    return [num/n for num in lst]
  return div_lst

