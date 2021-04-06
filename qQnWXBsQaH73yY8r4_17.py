
def kempner(n):
  l = []
  def factorial(num):
    if num == 1:
      return 1
    else:
      sum = 1
      for a in range(num):
        sum = sum * (num - a)
      return sum
  for a in range(1,n + 1):
    print(a)
    if factorial(a) % n == 0:
      l.append(a)
      print(l)
    l.sort()
  if len(l) > 0:
    return l[0]
  else:
    return n

