
def two_product(lst, n):
  def is_divisible(n, num):
    if n%num==0:
      return int(n/num)
    else:
      return False
  
  for num in lst:
    t = is_divisible(n, num)
    if t != False:
      if t in lst:
        return sorted([num, t])
  
  return None

