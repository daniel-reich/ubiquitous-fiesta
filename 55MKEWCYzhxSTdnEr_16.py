
def gcd(a, b):
  lst = []
  if a == b:
    return a
  else:
    for i in range(1,abs(a-b)+1):
      if a%i == 0 and b%i == 0:
        lst.append(i)
    return max(lst)

