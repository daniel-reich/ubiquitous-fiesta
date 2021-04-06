
def reorder_digits(lst, direction):
  def asc(x):
    return int("".join(sorted(d for d in str(x))))
    
  def desc(x):
    return int("".join(sorted((d for d in str(x)),reverse=True)))
    
  f = locals().get(direction)
  return [f(n) for n in lst]

