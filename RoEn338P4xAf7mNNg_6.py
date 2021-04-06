
def shortest_path(lst):
  def string(i):
    return lst[i]
  def row(n):
    return list(filter(lambda x: str(n) in string(x),range(0,len(lst))))[0]
  def col(n):
    return string(row(n)).index(str(n))
  def distance(a,b):
    return abs(row(a)-row(b)) + abs(col(a)-col(b))
  i = 1;
  total = 0;
  while i < 9:
    try:
      total += distance(i,i+1)
      i += 1
    except IndexError:
      return total
  return total

