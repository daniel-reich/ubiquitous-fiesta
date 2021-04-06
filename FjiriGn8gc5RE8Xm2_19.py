
def total_distance(fuel, fuel_usage, passengers, air_con):
  p = 1 + .05*passengers
  ac = 1 + .1*air_con
  return round(100 * fuel/(fuel_usage * p * ac), 1)

