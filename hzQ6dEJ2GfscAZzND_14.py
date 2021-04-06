
def factory(n):
  def div_by(lst):
    return [num/n for num in lst]
  
  return div_by

