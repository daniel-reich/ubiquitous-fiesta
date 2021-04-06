
def wash_hands(N, nM):
    times = N*30*nM
    sec = times * 21
    minutes = sec // 60
    sec = sec - (minutes*60)
    return "{} minutes and {} seconds".format(minutes,sec)

