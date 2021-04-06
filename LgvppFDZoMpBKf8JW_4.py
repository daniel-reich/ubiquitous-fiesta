
def digital_clock(seconds):
    seconds %= 86400
    h = str(seconds // 3600).zfill(2)
    seconds %= 3600
    m = str(seconds // 60).zfill(2)
    s = str(seconds % 60).zfill(2)
    return h + ':' + m + ':' + s

