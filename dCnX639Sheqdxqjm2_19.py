
def parallel_resistance(ohms):
    return round(1 / sum(1 / o for o in ohms), 1)

