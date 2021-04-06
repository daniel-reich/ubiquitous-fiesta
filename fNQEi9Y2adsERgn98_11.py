
def perimeter(lst):
  def myfunc (a,b):
    return (a-b)**2
  p = (sum(map(myfunc,lst[0],lst[1])))**0.5
  q = (sum(map(myfunc,lst[0],lst[2])))**0.5
  r = (sum(map(myfunc,lst[1],lst[2])))**0.5
  return round(p+q+r, 2)

