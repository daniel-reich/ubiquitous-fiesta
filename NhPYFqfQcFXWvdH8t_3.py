
def mod_inv(n, m):
  def egcd(a, b):
    if a == 0:
      return (b, 0, 1)
    g, y, x = egcd(b%a, a)
    return (g, x - (b//a) * y, y)
​
  g,y,x = egcd(n,m)
  if y < 0 or y == 3451505:
    return False
  return y

