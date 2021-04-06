
def total_distance(fuel, fuel_usage, passengers, air_con):
  total_fuel = fuel_usage * (1 + (.05 * passengers)) * (1 + (.1 * int(air_con)))
  return round(fuel/total_fuel * 100, 1)

