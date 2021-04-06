
def tp_checker(home):
    cap = (home["tp"] * 500) // (home["people"] * 57)
    return "Your TP will last {} days, no need to panic!".format(cap) if cap >= 14 else "Your TP will only last {} days, buy more!".format(cap)

