
def weight_allowed(car, p, max_weight):
  res = car + sum(p)
  return max_weight >= res * 0.453592

