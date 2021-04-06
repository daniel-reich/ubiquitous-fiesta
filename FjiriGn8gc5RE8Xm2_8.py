
def total_distance(fuel, fuel_usage, passengers, air_con):
    pct = passengers * .05
    fuel_usage = (1 + pct) * fuel_usage
    if air_con:
        fuel_usage = fuel_usage * 1.1
    return round(100*fuel/fuel_usage,1)

