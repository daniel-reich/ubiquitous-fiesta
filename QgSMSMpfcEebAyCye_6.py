
def time_saved(s_lim, s_avg, d):
    t1 = d / s_lim
    t2 = d / s_avg
    saved = (t1 - t2) * 60.
    return round(saved, 1)

