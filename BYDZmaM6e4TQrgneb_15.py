
def fib_fast(num):
  last = 1
  lastlast = 0
  out = 0
​
  for i in range(num-1):
      out = lastlast + last
      lastlast = last
      last = out
  return out

