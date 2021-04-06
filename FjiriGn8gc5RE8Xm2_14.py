
def total_distance(fuel, fuel_usage, passengers, air_con):
    extra = 1.10 if air_con == True else 1.0
    pass_num = 1.0 if passengers == 0 else passengers
    return round(fuel / ((fuel_usage * (1 + 0.05 * passengers)) * extra) * 100, 1)

