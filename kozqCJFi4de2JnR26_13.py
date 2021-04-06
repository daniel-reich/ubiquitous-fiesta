
def fib_str(n, f):
  for i in range(2, n):
    f += [f[i-1] + f[i-2]]
  return ', '.join(f)

