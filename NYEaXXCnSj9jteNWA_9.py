
def ave_spd(up_time, up_spd, down_spd):
    distance = up_spd * (up_time / 60)
    down_time = distance / down_spd
    return 2 * distance / (up_time / 60 + down_time)

