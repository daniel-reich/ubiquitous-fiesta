
def fib_str(n, f):
  if n==2: return ', '.join(f)
  meh = fib_str(n-1, f)
  meeh, meeeh = meh.split(', ')[-2:]
  return ', '.join([meh, meeeh+meeh])

