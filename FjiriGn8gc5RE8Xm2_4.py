
def total_distance(fuel, fuel_usage, passengers, air_con):
  ride=passengers*(fuel_usage*.05)+fuel_usage
  if air_con:ride=(ride)*1.1
  return round(fuel/ride*100,1)

