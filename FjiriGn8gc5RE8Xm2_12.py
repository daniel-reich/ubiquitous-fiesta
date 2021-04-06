
def total_distance(fuel, fuel_usage, passengers, air_con):
  inc_pass = 0.05*fuel_usage*passengers
  fuel_usage += inc_pass
  if air_con:
    fuel_usage *= 1.1
  return round(fuel/fuel_usage*100,1)

