
def is_polydivisible(n):
  s = str(n)
  return all(
    (int(s[:i]) / i).is_integer() 
    for i, _ in enumerate(s[1:], start=2)
  )

