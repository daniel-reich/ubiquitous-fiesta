
def ave_spd(up_time, up_spd, down_spd):
    line = up_spd * up_time / 60
    second_time = line / down_spd * 60
    return 2 * line / (second_time + up_time) * 60

