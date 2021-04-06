
def ave_spd(up_time, up_spd, down_spd):
    dist = up_time / 60 * up_spd
    down_time = dist / down_spd
    tot_time = down_time  + (up_time / 60)
    return (up_time / 60 / tot_time * up_spd) + (down_time / tot_time * down_spd)

