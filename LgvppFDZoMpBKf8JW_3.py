
def digital_clock(seconds):
    h = seconds//3600
    m = (seconds%3600)//60
    s = (seconds%3600)%60
    return "{:02d}:{:02d}:{:02d}".format(h if h < 24 else 00, m, s)

