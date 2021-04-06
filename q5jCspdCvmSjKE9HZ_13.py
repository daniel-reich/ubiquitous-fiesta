
def lcm_of_list(numbers):
  def gcd(x, y):
    while(y):
      x, y = y, x % y
    return x
  r=1
  for i in numbers:
    r*=i//gcd(r,i)
  return r

