
def total_distance(fuel, fuel_usage, passengers, air_con):
  t = fuel_usage + fuel_usage / 20 * passengers
  if air_con:
    t += t / 10
  return round(fuel * 100 / t, 1)

