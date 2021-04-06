
def lengthen(s1, s2):
    if len(s1) > len(s2):
        long, short = s1, s2
    else:
        long, short = s2, s1
    integer = len(long)//len(short)
    residual = len(long)%len(short)
    return integer*short + short[:residual]

