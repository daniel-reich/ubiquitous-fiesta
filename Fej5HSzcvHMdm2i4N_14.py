
def weight_allowed(car, p, max_weight):
  return car + sum(p) < round(max_weight / 0.453)

