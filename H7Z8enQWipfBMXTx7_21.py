
def fib_str(n, f):
  # Your recursive implementation of the code.
  if n == 2:
    return ", ".join(f)
  return fib_str(n-1, f + [f[-1] + f[-2]])

