
def prime_factors(num):
  def ip(x):
    return all(x%y for y in range(2,(x//2)+1))
​
  l = []
  while not ip(num):
    for x in (y for y in range(2,(num//2)+1) if ip(y)):
      if not num % x:
        l.append(x)
        num //= x
        break
  l.append(num)
  return l

