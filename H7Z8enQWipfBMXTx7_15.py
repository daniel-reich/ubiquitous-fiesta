
def fib_str(n, f):
  if len(f) == n:
    return ', '.join(f)
  f.append(f[-1]+f[-2])
  return fib_str(n, f)

