
def random(lst):
  x,y = lst
  d, r, s = ext_gcd(x,65535)
  if d!=1: return None
  a = (r*(y-1)) % 65535
  return (a*y+1) % 65535
​
def ext_gcd(a,b):
  a_a, a_b, b_a, b_b = 1, 0, 0, 1
  while a>0:
    a,b, a_a,a_b, b_a,b_b = b%a,a, b_a-(b//a)*a_a,b_b - (b//a)*a_b, a_a,a_b
  return b, b_a, b_b

