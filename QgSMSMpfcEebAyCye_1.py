
#def time_saved(s_lim, s_avg, d):
def time_saved(s_lim, s_avg, d):
    norm_time = (d / s_lim) * 60
    fast_time = (d / s_avg) * 60
    worth = norm_time - fast_time
    return round(worth, 1)

