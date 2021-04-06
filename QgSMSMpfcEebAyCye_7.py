
def time_saved(s_lim, s_avg, d):
    time = (d/s_lim) - (d/s_avg)
    return round(time * 60, 1)

