
def func(b, x):
    return (b + 1) * (x**(b + 1)) // (b + 1)
​
def integral(b, m, n):
  return func(b, n) - func(b, m)

