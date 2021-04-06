
def prime_divisors(n):
  box = []
  i = 2
  box1 = []
  while (i*i) <= n:
    if n%i==0:
      box.append(i)
      n//=i
    else:
      i += 1
  box.append(n)
  [box1.append(i) for i in box if i not in box1]
  return box1

