
def legendre(p, n):
  lst = []
  result = 0
  expo = 1
  while p ** expo <= n:
    result = int(n / (p ** expo))
    lst.append(result)
    expo += 1
​
​
  return (sum(lst))

