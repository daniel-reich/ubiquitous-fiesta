
def fact_of_fact(n):
  x = 1
  b = 1
  for i in range(n):
    for m in range(n - i):
      if m == (n - 1):
        break
      x = x * ((n - i) - m)
    b = b * x
    x = 1
  return(b)

