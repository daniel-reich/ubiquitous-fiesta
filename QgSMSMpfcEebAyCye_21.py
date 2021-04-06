
def time_saved(speed1, speed2, distance):
    result = lambda x: (distance / (x / 60))
    return round(result(speed1) - result(speed2), 1)

