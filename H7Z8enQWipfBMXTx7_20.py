
def fib_str(n, f):
  if len(f)==n:
    return ', '.join(f)
  return fib_str(n, f+[f[-1]+f[-2]])

