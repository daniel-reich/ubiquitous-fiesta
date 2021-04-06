
def wash_hands(N, nM):
    full_time = (N * 21) * (nM * 30)
    minutes = full_time // 60
    seconds = full_time % 60
    return str(minutes) + " minutes and " + str(seconds) + " seconds"

