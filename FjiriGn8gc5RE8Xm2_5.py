
def total_distance(fuel, fuel_usage, passengers, air_con):
  total_fuel_usage = (fuel_usage*(1 + 0.05*passengers))*(1 + 0.1*air_con)
  return round((fuel/total_fuel_usage)*100,1)

