
def total_distance(fuel, fuel_usage, passengers, air_con):
  fuel_usage += fuel_usage/20*passengers
  fuel_usage += fuel_usage/10*(air_con==True)
  return round(fuel/fuel_usage*100,1)

