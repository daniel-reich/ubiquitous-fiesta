
def total_distance(fuel, fuel_usage, passengers, air_con):
  return round(100*fuel/(fuel_usage*(1+0.05*passengers)*(1+.1*air_con)),1)

