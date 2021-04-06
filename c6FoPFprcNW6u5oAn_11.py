
def farey(n):
  def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)
  def hdiv(x):
    d = list(map(int, x.split('/')))
    if d[0] == 0 or d[0] == d[1]:
      return d[1] == 1
    return gcd(d[0], d[1]) == 1
  r = [str(x) + '/' + str(y) for x in range(n) for y in range(1, n + 1) if x <= y]
  return list(filter(hdiv, sorted(r, key = eval)))

