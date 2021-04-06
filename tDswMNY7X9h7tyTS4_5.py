
def fact(n):
  return 1 if not n else n * fact(n - 1)
​
def pascals_triangle(n):
  pl = []
​
  for r in range(n):
    c = r + 1
    for c in range(c):
      n, k = r, c
      pl.append(fact(n) / (fact(k) * fact(n - k)))
​
  return pl

