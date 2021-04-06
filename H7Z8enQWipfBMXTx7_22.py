
def fib_str(n, f):
  if n == 2:
    return ", ".join(f)
  else:
    f.append(f[-1]+f[-2])
    return fib_str(n-1,f)

