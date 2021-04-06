
def digital_clock(seconds):
    return "{:02d}:{:02d}:{:02d}".format(s//60//60%24, s//60%60, s%60)

