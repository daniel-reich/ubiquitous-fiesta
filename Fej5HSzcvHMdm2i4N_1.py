
def weight_allowed(car, passengers, max_weight):
  return car + sum(passengers) < 2.2 * max_weight

