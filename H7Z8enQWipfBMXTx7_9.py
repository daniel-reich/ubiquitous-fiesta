
def fib_str(n, f):
  return ", ".join(f) if len(f)==n else fib_str(n, f+[f[-1]+f[-2]])

