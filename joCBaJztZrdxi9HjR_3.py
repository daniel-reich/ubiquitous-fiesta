
def tp_checker(home):
    import math
    d = math.floor((home['tp'] * 500) / (int(home['people']) * 57))
    if d < 14:
        return "Your TP will only last {} days, buy more!".format(d)
    else:
        return "Your TP will last {} days, no need to panic!".format(d)

