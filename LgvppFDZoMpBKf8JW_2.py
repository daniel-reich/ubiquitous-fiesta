
def digital_clock(s):
    return '{:02}:{:02}:{:02}'.format(s//3600%24, s//60%60, s%3600%60)

