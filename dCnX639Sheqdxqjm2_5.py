
def parallel_resistance(lst):
    return round(1 / sum(1/n for n in lst), 1)

