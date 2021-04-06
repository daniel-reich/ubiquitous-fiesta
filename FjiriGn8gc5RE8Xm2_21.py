
def total_distance(fuel, fuel_usage, passengers, air_con):
  fuel_usage += fuel_usage * passengers * 0.05
  fuel_usage += fuel_usage * 0.1 * air_con
  return round(fuel / fuel_usage * 100, 1)

