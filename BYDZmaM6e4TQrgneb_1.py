
def fibFast(n):
  s = 5**0.5
  P = (1 + s)/2
  p = (1 - s)/2
  return round((P**n - p**n) / s)

