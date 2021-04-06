
def last(a, n):
  return a[len(a)-n:] if a and not n > len(a) else "invalid"

