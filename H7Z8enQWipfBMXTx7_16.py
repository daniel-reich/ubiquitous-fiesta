
def fib_str(n, f):
  if n == 0:
    return ", ".join(f[0:-2])
  return fib_str(n-1, f + [f[len(f)-1]+f[len(f)-2]])

