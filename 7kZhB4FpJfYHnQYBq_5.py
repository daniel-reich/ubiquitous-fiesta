
def lcm_three(num):
  def gcd(x, y): 
    while(y):
      x, y = y, x % y
    return x
  r=1
  for i in range(3):
    r*=num[i]//gcd(r,num[i])
  return r

