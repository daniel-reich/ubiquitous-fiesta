
def fibo(n):
  a, b = 1, 1
  l = [a,b]
  for i in range(n//2):
    a+=b
    b+=a
    l.append(a)
    l.append(b)
  return l[n-1]

