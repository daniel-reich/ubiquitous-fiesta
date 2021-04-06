
def weight_allowed(car, p, max_weight):
  x = sum(p)
  return (car + x) * 0.453592 < max_weight

