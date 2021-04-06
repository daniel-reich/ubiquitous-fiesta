
factorial = lambda x: 1 if not x else x * factorial(x-1)
​
def filter_factorials(n):
  fs = [ factorial(x) for x in range(1,max(n)) ]
  return [ e for e in n if e in fs ]

