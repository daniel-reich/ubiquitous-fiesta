
def fib(n):
  a = [0, 1]
  if n in a: return a[n]
  for i in range(2, n+1):
      a.append(a[-1]+a[-2])
  return a[-1]

