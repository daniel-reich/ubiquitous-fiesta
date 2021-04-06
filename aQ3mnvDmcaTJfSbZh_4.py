
def bw_transform(text):
    bwt = ""
    bwm = [text]
    for i in range(1, len(text)):
        bwm.append( bwm[-1][1:] + bwm[-1][0] )
    bwm = sorted(bwm)
    for t in bwm:
        bwt += t[-1]
    return bwt

